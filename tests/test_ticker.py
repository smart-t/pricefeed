import datetime

import pytest

from pricefeed import Pricefeed

t_set = lambda: datetime.datetime.now().astimezone().replace(microsecond=0)
t_diff = lambda t: str(t_set() - t)


def test_constructor():
    AAPL_ticker = Pricefeed("AAPL", 100)
    assert AAPL_ticker.name == "AAPL"
    assert AAPL_ticker.price == 100.0
    assert AAPL_ticker.delay == 1000.0
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
    print(
        f"\nNewprice: {newprice} within 1% from Startprice, which was at {startprice}"
    )
    assert newprice <= 101 and newprice >= 99


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
