import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mplfinance as mpf
import vnquant.DataLoader as dl
from datetime import datetime
import stockstats
from stockstats import StockDataFrame


class plot_price_1y_class(object):
    def __init__(self, symbol):
        self.symbol = symbol

    def PlotPrice1y(self):
        start = '2021-01-27'
        now = datetime.now()
        end = now.strftime("%Y-%m-%d")
        loader = dl.DataLoader(self.symbol, start, end, data_source='VND', minimal=True)
        pricedata = loader.download()

        openPrice = pricedata['open'].dropna()
        closePrice = pricedata['close'].dropna()
        highPrice = pricedata['high'].dropna()
        lowPrice = pricedata['low'].dropna()
        volumeDaily = pricedata['volume'].dropna()

        dailyInfo = pd.DataFrame()
        # dailyInfo = pd.concat([openPrice,closePrice,highPrice, lowPrice, volumeDaily], ignore_index=True,  axis=1)
        dailyInfo['Open'] = openPrice
        dailyInfo['High'] = highPrice
        dailyInfo['Low'] = lowPrice
        dailyInfo['Close'] = closePrice
        dailyInfo['Volume'] = volumeDaily
        # ['open', 'high', 'low', 'close', 'volume']
        # dailyInfo = closePrice
        # Plot the candle price chart of the stock
        self.daily = dailyInfo.apply(pd.to_numeric, errors='coerce')

        # mav: 22 days average
        fig, axes = mpf.plot(self.daily, type='candle', style='charles', volume=True, mav=22, returnfig=True)
        title = ('%s | 1 year price chart') % (self.symbol)
        axes[0].set_title(title)

        plt.show()
        return self.daily


if __name__ == '__main__':
    symbol = input('Please enter a symbol: ')

    #start = input('Enter the starting date (yyyy-mm-dd): ')
    symbol = symbol.upper()
    stock = plot_price_1y_class(symbol)
    figure = stock.PlotPrice1y()
    # print(HAH.head(3))

    print(figure.info())