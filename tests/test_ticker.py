import datetime

import pytest

from pricefeed import Pricefeed

t_set = lambda: datetime.datetime.now().astimezone().replace(microsecond=0)
t_diff = lambda t: str(t_set() - t)


def test_constructor():
    AAPL_ticker = Pricefeed("AAPL", 100)
    assert AAPL_ticker.name == "AAPL"
    assert AAPL_ticker.price == 100.0
    assert AAPL_ticker.delay == 0.0
    assert AAPL_ticker.vol == 0.01
    print(
        f'\nPricefeed("AAPL", 100): name={AAPL_ticker.name}, price={AAPL_ticker.price}, delay={AAPL_ticker.delay}, vol={AAPL_ticker.vol} (correct defaults for delay and vol)'
    )


def test_feeddelay():
    AAPL_ticker = Pricefeed("Apple", 100, 1000, 0.01)
    t = t_set()
    for _ in range(2):
        _ = next(AAPL_ticker)
    timeOfTwoTicks = t_diff(t)
    assert timeOfTwoTicks == "0:00:02"
    print(f"\nYielding two prices took {timeOfTwoTicks} with one tick per second.")


def test_firstprice():
    AAPL_ticker = Pricefeed("Apple", 100, 1000, 0.01)
    startprice = next(
        AAPL_ticker
    )  # Ignore first tick as this is the price used in the constructor
    newprice = next(AAPL_ticker)
    assert newprice <= 101 and newprice >= 99
    print(
        f"\nNewprice: {newprice} within 1% from Startprice, which was at {startprice}"
    )


def test_avgprice():
    AAPL_ticker = Pricefeed("Apple", 100, 0, 0.01)
    sumPrice = 0.0
    print(" ")
    for i in range(4):
        sumPrice += AAPL_ticker.price
        print(f"{i}: {AAPL_ticker.price}")
        next(AAPL_ticker)

    avg = sumPrice / 4
    assert AAPL_ticker.avgPrice == avg
    print(
        f"Calculated average price ={avg}, avg price from the feed ={AAPL_ticker.avgPrice}"
    )


def test_maxprice():
    AAPL_ticker = Pricefeed("Apple", 100, 0, 0.01)
    maxprice = 0.0
    print(" ")
    for i in range(4):
        p = AAPL_ticker.price
        if p >= maxprice:
            maxprice = p
        print(f"{i}: {AAPL_ticker.price}")
        next(AAPL_ticker)

    assert AAPL_ticker.maxPrice == maxprice
    print(
        f"Found max price ={maxprice}, max price from the feed ={AAPL_ticker.maxPrice}"
    )


def test_minprice():
    AAPL_ticker = Pricefeed("Apple", 100, 0, 0.01)
    minprice = 0.0
    print(" ")
    for i in range(4):
        p = AAPL_ticker.price
        if p <= minprice or minprice == 0:
            minprice = p
        print(f"{i}: {AAPL_ticker.price}")
        next(AAPL_ticker)

    assert AAPL_ticker.minPrice == minprice
    print(
        f"Found min price ={minprice}, min price from the feed ={AAPL_ticker.minPrice}"
    )


def test_getsetname():
    AAPL_ticker = Pricefeed("Apple", 100, 1000, 0.01)
    thename = AAPL_ticker.name
    assert thename == "Apple"
    AAPL_ticker.name = "Google"
    newname = AAPL_ticker.name
    assert newname == "Google"


def test_getsetprice():
    AAPL_ticker = Pricefeed("Apple", 100, 1000, 0.01)
    theprice = AAPL_ticker.price
    assert theprice == 100
    AAPL_ticker.price = 200
    newprice = AAPL_ticker.price
    assert newprice == 200


def test_getsetdelay():
    AAPL_ticker = Pricefeed("Apple", 100, 1000, 0.01)
    thedelay = AAPL_ticker.delay
    assert thedelay == 1000
    AAPL_ticker.delay = 500
    newdelay = AAPL_ticker.delay
    assert newdelay == 500


def test_getsetvol():
    AAPL_ticker = Pricefeed("Apple", 100, 1000, 0.01)
    thevol = AAPL_ticker.vol
    assert thevol == 0.01
    AAPL_ticker.vol = 0.001
    newvol = AAPL_ticker.vol
    assert newvol == 0.001


if __name__ == "__main__":
    pytest.main()
