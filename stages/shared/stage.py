class Stage:

    def __init__(self, step):
        self.step = step

    def __call__(self, *args, **kwargs):
        self.pre_run()
        successful = self.run()
        if successful:
            self.after_run()

    def pre_run(self):
        pass

    def run(self) -> bool:
        pass

    def after_run(self):
        pass
