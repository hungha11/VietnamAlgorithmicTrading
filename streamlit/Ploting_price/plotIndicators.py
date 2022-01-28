import pandas as pd
import numpy as np
import vnquant.DataLoader as dl
from datetime import datetime
import stockstats
from  stockstats import StockDataFrame
import matplotlib.pyplot as plt


class plot_the_indicator(object):
    def __init__(self, symbol):
        self.symbol = symbol

    def get_data_for_indicators(self):
        start = '2021-01-27'
        now = datetime.now()
        end = now.strftime("%Y-%m-%d")
        loader = dl.DataLoader(self.symbol, start, end, data_source='VND', minimal=True)
        data = loader.download()
        close_data = data.dropna()
        self.stock = StockDataFrame(close_data)

        return self.stock

    def plot_momentum(self):
        target = self.stock
        rsi = target.get('rsi')
        rsi = rsi.dropna()
        rsi = rsi[1:]
        macd =target.get('macd')
        macds =target.get('macds')
        macdh =target.get('macdh')
        macd = macd[1:]
        macds = macds[1:]
        macdh = macdh[1:]

        fig, (ax1, ax2) = plt.subplots(2, 1)

        ax1.plot(macd, label = 'MACD')

        ax1.plot(macds, label = 'MACDS')
        ax1.plot(macdh, label = 'MACDH')
        ax1.legend()
        #ax1[0].legend(loc='MACD')
        ax1.set_ylabel('MACD line')


        ax2.plot(rsi, label = 'RSI')
        ax2.yaxis.grid(True)
        ax2.set_ylabel('RSI')
        ax2.legend()
        #ax2.set_xlim(40, 80)
        #plt.plot(x1,y1)
        # plt.plot(y2)
        #plt.legend()
        plt.show()


        #return self.rsi, macd



if __name__ == '__main__':
    stock = plot_the_indicator('VND')
    symbol = stock.get_data_for_indicators()
    print(symbol)
    fig = stock.plot_momentum()
