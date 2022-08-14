import logging
from typing import List
from shared import Stage
from apps.stage import last_stage, add_stage, update_end_date, models as stage_model
from apps.city import models as city_model
from services.database import engine
from stage.stages import *


class StageRunner:
    ALL_STAGES = {
        InitialStage: True,
        ExternalSource1: False,
        ExternalSource2: False,
        # NlpNer: False, # todo failed
    }

    def __init__(self, stages: List[Stage] = None):
        if stages is None:
            stages = StageRunner.ALL_STAGES
        self.stages: dict = stages
        self.step: int = None
        self.__start()

    def __start(self):
        self.pre_run()
        self.run()
        self.after_run()

    def pre_run(self):
        city_model.Base.metadata.create_all(bind=engine)
        stage_model.Base.metadata.create_all(bind=engine)
        last_step = last_stage()
        self.step = (0 if not last_step else last_step.step) + 1
        add_stage(self.step)

    def run(self):
        for stage, necessary in self.stages.items():
            try:
                stage(self.step, necessary)()
            except Exception as e:
                logging.error(e)
                if necessary:
                    return False

    def after_run(self):
        update_end_date(self.step)


StageRunner()
