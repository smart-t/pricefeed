# PriceFeed

This is a generator for random price feeds that can be used to generate a new
price at will or at predefined time intervals. The PriceFeed object will also
maintain statistics on all the prices that it generated.

A typical use-case is in a development environment where you would like to
mimic a pricefeed.

You can install the package via **PyPI** or from **source**.

### Install from PyPI

```bash
pip install pricefeed
```

### Install from Source (GitHub)

```bash
git clone https://github.com/smart-t/pricefeed.git
cd pricefeed
pip install .
```

### Example: How to use this package

```bash
import pricefeed as pf

AAPL_ticker = pf.Pricefeed("AAPL", 235.0, 500, 0.001)
for i in range(10):
  print(f"{i} : {next(AAPL_ticker)}")
```

The above script will generate a new price every 500 miliseconds and completes
a list with 10 simulated 'AAPL' stock prices starting at $235.0. The 4th
argument is used to indicate how volatile the stock movement will be.

The generated prices are designed to stay relatively close to the given start
price.

The third and fourth properties (delay and vol) are optional, and if not
provided they default to `1000ms` (`1sec`) and a volatility of `0.01`.

## Contributions

This is an opensource project where you are invited to contribute and help
evolve the pricefeed as we go.
