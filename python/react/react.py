class InputCell(object):
    def __init__(self, initial_value):
        self._value = initial_value
        self.notify_receivers = []

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, v):
        self._value = v
        self.notify()

    def notify(self):
        if len(self.notify_receivers) > 0:
            for notify_rec in self.notify_receivers:
                notify_rec.update()


class ComputeCell(object):
    def __init__(self, inputs, compute_function):
        self.inputs = inputs
        self.compute_function = compute_function
        self.notify_receivers = []
        self.callbacks = []
        self._value = self.value
        for input in inputs:
            input.notify_receivers.append(self)

    @property
    def value(self):
        return self.compute_function([i.value for i in self.inputs])

    def update(self):
        old_value = self._value
        self._value = self.value
        if old_value != self._value:
            for c in self.callbacks:
                c(self._value)
        if len(self.notify_receivers) > 0:
            for notify_rec in self.notify_receivers:
                notify_rec.update()

    def add_callback(self, callback):
        self.callbacks.append(callback)

    def remove_callback(self, callback):
        if callback in self.callbacks:
            self.callbacks.remove(callback)
