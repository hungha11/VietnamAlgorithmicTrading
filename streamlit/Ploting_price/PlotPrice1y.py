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

    def get_data_1y(self):

        start = '2021-01-27'
        now = datetime.now()
        end = now.strftime("%Y-%m-%d")
        loader = dl.DataLoader(self.symbol, start, end, data_source='VND', minimal=True)
        data = loader.download()
        close_data = data.dropna()
        historical_data = pd.DataFrame(close_data)
        historical_data.reset_index()
        self.dfplot = historical_data[['open', 'high', 'low', 'close', 'volume']]
        self.dfplot.index.name = 'Date'
        # del dfplot['Symbols']
        self.dfplot.shape
        csv = self.dfplot.to_csv('Price 1 year', index=True)
        return self.dfplot


    def plot_candle_1y(self):
        #Prepare the data
        data = pd.read_csv('/Users/haquochung/OneDrive/OneDrive - RMIT University/Home/PyCharm/VietnamAlgorithmicTrading/streamlit/Ploting_price/Price 1 year for Ploting')
        SYMBOL = data.loc[0][1]
        data= data.drop(data.index[0])
        data= data.drop(data.index[0])
        df = data.rename(columns={'Attributes': 'Date', 'open': 'Open' , 'high': 'High','low': 'Low','close': 'Close','volume': 'Volume' })
        title = ('%s | 1 year price chart') % (SYMBOL)
        df.index = pd.DatetimeIndex(df['Date'])
        df.drop('Date', axis=1, inplace=True)
        df.shape


        #Plot the candle price chart of the stock
        self.daily = df.apply(pd.to_numeric, errors='coerce')
        #fig, axes = mpf.plot(daily, type='candle',style = 'charles' ,volume = True, mav = mav_tuple, title = title , figsize = (10,8))
        # Configure chart legend and title

        #mav: 22 days average
        fig, axes = mpf.plot(self.daily, type='candle',style = 'charles' ,volume = True, mav = 22, returnfig=True)
        axes[0].set_title(title)

        plt.show()
        return self.daily


if __name__ == '__main__':
    symbol = input('Please enter a symbol: ')

    #start = input('Enter the starting date (yyyy-mm-dd): ')
    symbol = symbol.upper()
    stock = plot_price_1y_class(symbol)
    target = stock.get_data_1y()
    figure = stock.plot_candle_1y()
    # print(HAH.head(3))

    print(figure.info())