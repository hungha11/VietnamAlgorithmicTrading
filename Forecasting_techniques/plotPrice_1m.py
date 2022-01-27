import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mplfinance as mpf
import vnquant.DataLoader as dl
from datetime import datetime
import stockstats
from stockstats import StockDataFrame



def get_data(symbol):
    start = '2021-12-27'
    now = datetime.now()
    end = now.strftime("%Y-%m-%d")
    loader = dl.DataLoader(symbol, start, end, data_source='VND', minimal=True)
    data = loader.download()
    close_data = data.dropna()
    historical_data = pd.DataFrame(close_data)
    historical_data.reset_index()
    dfplot = historical_data[['open', 'high', 'low', 'close', 'volume']]
    dfplot.index.name = 'Date'
    # del dfplot['Symbols']
    dfplot.shape
    csv = dfplot.to_csv('Price 1 month', index=True)
    return dfplot


def plot_candle_1y():

    #Prepare the data
    data = pd.read_csv('/Users/haquochung/OneDrive/OneDrive - RMIT University/Home/PyCharm/VietnamAlgorithmicTrading/Forecasting_techniques/Price 1 month')
    SYMBOL = data.loc[0][1]
    data= data.drop(data.index[0])
    data= data.drop(data.index[0])
    df = data.rename(columns={'Attributes': 'Date', 'open': 'Open' , 'high': 'High','low': 'Low','close': 'Close','volume': 'Volume' })
    title = ('%s | 1 month price chart') % (SYMBOL)
    df.index = pd.DatetimeIndex(df['Date'])
    df.drop('Date', axis=1, inplace=True)
    df.shape


    #Plot the candle price chart of the stock
    daily = df.apply(pd.to_numeric, errors='coerce')
    mav_tuple = (3,5,22)
    #fig, axes = mpf.plot(daily, type='candle',style = 'charles' ,volume = True, mav = mav_tuple, title = title , figsize = (10,8))
    # Configure chart legend and title
    fig, axes = mpf.plot(daily, type='candle', style = 'charles',volume = True, mav=3, returnfig=True)
    # Configure chart legend and title
    axes[0].legend('3')
    axes[0].set_title(title)

    # Save figure to file
    #fig.savefig(path_to_figure)
    #mpf.plot(daily, type='candle',style = 'charles' ,volume = True, mav = mav_tuple, title = title)
    plt.show()
    return daily


if __name__ == '__main__':
    symbol = input('Please enter a symbol: ')
    #start = input('Enter the starting date (yyyy-mm-dd): ')
    symbol = symbol.upper()
    target = get_data(symbol)
    # print(HAH.head(3))
    figure = plot_candle_1y()
    print(figure.info())