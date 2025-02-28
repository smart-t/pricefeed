import pytest

from pricefeed import Pricefeed


def test_firstprice():
    AAPL_ticker = Pricefeed("Apple", 100, 1000, 0.01)
    newprice = next(AAPL_ticker)
    assert newprice <= 101 and newprice >= 99


if __name__ == "__main__":
    pytest.main()
