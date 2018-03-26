import bisect

class RangeException(Exception):
    def __init__(self, message):
        super().__init__(message)

class TypeException(Exception):
    def __init__(self, message):
        super().__init__(message)

class TempTracker:
    # record temperatures in fahrenheit (0-110)

    def __init__(self):
        self.temps = []
        self.mean = 0.0

    def update_mean(self, temp):
        size = len(self.temps)
        self.mean = (size * self.mean + temp) / (size + 1)

    def insert(self, temp):
        if type(temp) is not int:
            raise TypeException('{0} ({1}) is not a valid integer'.format(temp, type(temp)))
        if temp > 110 or temp < 0:
            raise RangeException('{0} is not in valid range 0 - 110 degrees Fahrenheit'.format(temp))
        self.update_mean(temp)
        bisect.insort(self.temps, temp)

    def get_max(self):
        return self.temps[-1]

    def get_min(self):
        return self.temps[0]

    #return float.
    def get_mean(self):
        return self.mean