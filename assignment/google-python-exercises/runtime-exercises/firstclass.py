""" This is my first python class """
class firstclass:
    """ Initializing of method """
    def __init__(self):
        self._bar = 1
    @property
    def bar(self):
        return self._bar
    @bar.setter
    def bar(self, value):
        self._bar = value





