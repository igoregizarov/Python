from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def s_sum(self):
        pass


class Manto(Clothes):
    @property
    def s_sum(self):
        return self.param / 6.5 + 0.5


class Suit(Clothes):
    @property
    def s_sum(self):
        return 2 * self.param + 0.5


var_1 = Manto(6.5)
print(var_1.s_sum)

var_2 = Suit(6.5)
print(var_2.s_sum)