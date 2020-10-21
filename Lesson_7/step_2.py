from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def tissue_cost(self):
        pass


class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def tissue_cost(self):
        return round(self.v / 6.5 + 0.5, 2)


class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def tissue_cost(self):
        return round(2 * self.h + 0.3, 2)


coat1, suit1 = Coat(4), Suit(4)

print(f'{str(coat1.tissue_cost)} for coat and {str(suit1.tissue_cost)} for suit.')
