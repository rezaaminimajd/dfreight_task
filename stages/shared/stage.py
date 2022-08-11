class Stage:

    def __init__(self, step):
        self.step = step

    def __call__(self, *args, **kwargs):
        self.pre_run()
        self.run()
        self.after_run()

    def pre_run(self):
        pass

    def run(self):
        pass

    def after_run(self):
        pass
