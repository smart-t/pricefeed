import random as r
from time import sleep


class Pricefeed:
    def __init__(self, name: str, price: float, delay: float, vol: float):
        self.name = name
        self.price = price
        self.delay = delay
        self.vol = vol

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
