import random as r
from time import sleep


class Pricefeed:
    def __init__(self, name, price, delay=1000.0, vol=0.01) -> None:
        self.name = name
        self.price = price
        self.delay = delay
        self.vol = vol

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value: float):
        self._price = value

    @property
    def delay(self):
        return self._delay

    @delay.setter
    def delay(self, value: float):
        self._delay = value

    @property
    def vol(self):
        return self._vol

    @vol.setter
    def vol(self, value: float):
        self._vol = value

    def __iter__(self):
        return self

    def __next__(self):
        newprice = self.price

        randomvalue = r.random()
        changepercentage = 2 * self.vol * randomvalue
        if changepercentage > self.vol:
            changepercentage -= 2 * self.vol

        self.price *= 1 + changepercentage
        sleep(self.delay / 1000)
        return newprice

    def __str__(self):
        return f"{self.name}: {self.price}"
