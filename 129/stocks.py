import requests
from collections import Counter

STOCK_DATA = "https://bites-data.s3.us-east-2.amazonaws.com/stocks.json"

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(STOCK_DATA).json()


# your turn:


def _cap_str_to_mln_float(cap):
    """If cap = 'n/a' return 0, else:
    - strip off leading '$',
    - if 'M' in cap value, strip it off and return value as float,
    - if 'B', strip it off, multiply by 1,000 and return
      value as float"""
    if cap == "n/a":
        return 0
    else:
        clean_cap = float(cap.strip("$BM"))

        if "B" in cap:
            clean_cap *= 1000

        return clean_cap


def get_industry_cap(industry):
    """Return the sum of all cap values for given industry, use
    the _cap_str_to_mln_float to parse the cap values,
    return a float with 2 digit precision"""

    sum_cap = sum(
        [
            _cap_str_to_mln_float(item.get("cap"))
            for item in data
            if item.get("industry") == industry
        ]
    )

    return round(sum_cap, 2)


def get_stock_symbol_with_highest_cap():
    """Return the stock symbol (e.g. PACD) with the highest cap, use
    the _cap_str_to_mln_float to parse the cap values"""

    stocks_list = [
        (stock.get("symbol"), _cap_str_to_mln_float(stock.get("cap"))) for stock in data
    ]

    return max(stocks_list, key=lambda item: item[1])[0]


def get_sectors_with_max_and_min_stocks():
    """Return a tuple of the sectors with most and least stocks,
    discard n/a"""
    c = Counter([stock["sector"] for stock in data if stock["sector"] != "n/a"])

    max_stocks = c.most_common(1)[0][0]
    min_stocks = c.most_common().pop()[0]

    return (max_stocks, min_stocks)
