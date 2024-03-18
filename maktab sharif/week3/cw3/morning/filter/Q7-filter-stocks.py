def filter_profitable_stocks(stocks):
    return dict(filter(lambda stock: ((stock[1][-1] - stock[1][0]) / stock[1][0]) * 100 > 25, stocks.items()))


stock_data = {
    "AAPL": [230.56, 231.78, 232.9, 234.12, 235.34],
    "GOOGL": [230.56, 231.78, 232.9, 234.12, 600.34],
    "MSFT": [6, 7, 7.6, 7.8, 9],
    "BTC": [16, 23, 34, 44, 73]
}
print(filter_profitable_stocks(stock_data))