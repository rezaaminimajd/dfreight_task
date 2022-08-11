from typing import List
from stage import Stage
from apps.stage import last_stage, add_stage, update_end_date


class StageRunner:
    ALL_STAGES = []

    def __init__(self, stages: List[Stage] = None):
        if stages is None:
            stages = StageRunner.ALL_STAGES
        self.stages: list = stages
        self.step: int = None

    def __call__(self, *args, **kwargs):
        self.pre_run()
        self.run()
        self.after_run()

    def pre_run(self):
        self.step = last_stage() + 1
        add_stage(self.step)

    def run(self):
        for stage in self.stages:
            stage(self.step)

    def after_run(self):
        update_end_date(self.step)
