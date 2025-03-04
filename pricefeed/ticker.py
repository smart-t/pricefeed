import random as r
from time import sleep


class Pricefeed:
    def __init__(self, name, price, delay=0.0, vol=0.01) -> None:
        self._name = name
        self._price = price
        self._delay = delay
        self._vol = vol
        self._sumPrices = 0.0
        self._minPrice = 0.0
        self._maxPrice = 0.0
        self._numberOfSamples = 0
        self._avgPrice = 0.0

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

    @property
    def avgPrice(self):
        return self._avgPrice

    @avgPrice.setter
    def avgPrice(self, value: float):
        self._avgPrice = value

    @property
    def maxPrice(self):
        return self._maxPrice

    @maxPrice.setter
    def maxPrice(self, value: float):
        self._maxPrice = value

    @property
    def minPrice(self):
        return self._minPrice

    @minPrice.setter
    def minPrice(self, value: float):
        self._minPrice = value

    def __iter__(self):
        return self

    def __next__(self):
        newprice = self.price

        if newprice >= self.maxPrice:
            self.maxPrice = newprice

        if newprice <= self.minPrice or self.minPrice == 0:
            self.minPrice = newprice

        randomvalue = r.random()
        changepercentage = 2 * self.vol * randomvalue
        if changepercentage > self.vol:
            changepercentage -= 2 * self.vol

        self._numberOfSamples += 1
        self._sumPrices += self.price
        self.avgPrice = self._sumPrices / self._numberOfSamples

        self.price *= 1 + changepercentage

        if self.delay > 0:  # only delay when parameter is provided
            sleep(self.delay / 1000)
        return newprice

    def __str__(self):
        return f"{self.name}: {self.price}"
