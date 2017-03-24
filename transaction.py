class Charge:
    def __init__(self, val = 0):
        self._value = val
    @property
    def value(self):
        return round(self._value, 2)

class Account:
    def __init__(self, val = 0):
        if val < 0:
            raise Exception
        self._total = val
        self._charges = list()

    def Append(self, val):
        self._charges.append(Charge(val))
        self._total += val
    def Subtract(self, val):
        self._charges.append(Charge(-val))
        self._total -= val

    @property
    def total(self):
        return round(self._total, 2)
