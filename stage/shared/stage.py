class Stage:

    def __init__(self, step, necessary):
        self.step = step
        self.necessary = necessary

    def __call__(self, *args, **kwargs):
        self.pre_run()
        successful = self.run()
        if successful:
            self.after_run()
        return successful

    def pre_run(self):
        pass

    def run(self) -> bool:
        pass

    def after_run(self):
        pass
