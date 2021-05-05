'''
model.py - Default model for the simulation
'''

from player import default_player

class ModelObserved:
    def __init__(self, name):
        self._observers = []
        self._name = name
        self._output = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)

        except ValueError:
            print("Observer is already not in the list of observers")

    def notify(self):
        for observer in self._observers:
            observer.update_text(self)

    @property
    def output(self):
        return self._output

    @output.setter
    def output(self, output):
        self._output.append(output)
        self.notify()

    def clear(self):
        self._output = []

    def new_output(self, output):
        self.clear()
        self._output.append(output)

model = {
    "player": default_player
    ,"enemy": None
    ,"cleanText": False
    ,"inBattle": False
    ,"initiative": False
    ,"sleep_count": 6
    ,"critHit": False
    ,"output": ModelObserved("output")
}

if __name__ == '__main__':
    for key, value in model.items():
        print(key, ":", value)