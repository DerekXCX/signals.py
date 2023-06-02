import signals

class create:
    def __init__(self):
        self.testing_signal = signals.create()
    def fireSignal(self):
        self.testing_signal.Fire("Fired connection")
