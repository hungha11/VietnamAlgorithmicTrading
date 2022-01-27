import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mplfinance as mpf
import vnquant.DataLoader as dl
from datetime import datetime
import stockstats
from stockstats import StockDataFrame

def get_data(symbol):
    start = '2020-12-01'
    now = datetime.now()
    end = now.strftime("%Y-%m-%d")
    loader = dl.DataLoader(symbol, start, end, data_source='VND', minimal=True)
    data = loader.download()
    close_data = data.dropna()
    historical_data = pd.DataFrame(close_data)
    historical_data['PctChangeDaily'] = historical_data['close'].pct_change()
    historical_data['PctChangeDaily'] = round(historical_data['PctChangeDaily'],4)
    historical_data = historical_data[1:]
    return historical_data


def plot_daily_change(symbol):
    data = get_data(symbol)
    title = '%s | Price daily change'%(symbol)
    data['PctChangeDaily'].plot(title = title, figsize = (10,6))
    plt.show()
    return data

def plot_candlestick(symbol):
    df = get_data(symbol)
    #df = df.drop('PctChangeDaily')
    stock = StockDataFrame(df)
    df.drop('PctChangeDaily', axis=1, inplace=True)
    dfplot = df[['open','high','low','close','volume']]
    df.index.name = 'Date'
    #df.drop(df.index['Symbols'])
    #df.shape
    csv = df.to_csv('Data_test', index = True)
    #mpf.plot(dfplot, type = 'candle')
    return  dfplot

def plot_bollingerband(symbol):
    df = get_data(symbol)
    stock = StockDataFrame(df)
    boll = stock['boll']
    boll_ub = stock['boll_ub']
    boll_lb = stock['boll_lb']
    title = ('%s | Bollinger band')%(symbol)
    #indicators = stock['boll'].plot(title = title, figsize = (10,6))
    plt.plot(boll, label='Baseline', linestyle="-")
    plt.plot(boll_ub, label='Upper band', linestyle="-.")
    plt.plot(boll_lb, label='Lower band', linestyle="--")
    plt.title(title)
    plt.legend()
    plt.show()

def plot_momentum(symbol):
    df = get_data(symbol)
    stock = StockDataFrame(df)


    # #volume variation
    # vol = stock['volume']
    # VLvar = stock['vr_6']
    
    #RSI indicator
    RSI = stock['rsi_3']
    RSI = RSI.dropna()
    #SMA
    SMA = stock['macd']


    #plot
    title = ('%s | Momentum indicators') % (symbol)

    fig, (ax1,ax2) = plt.subplots(2)
    ax1.plot(RSI)
    ax2.plot(SMA)
    fig.suptitle(title)
    plt.legend()
    plt.show()
    

if __name__ == '__main__':
    #VHM = plot_daily_change('VHM')
    #print(VHM)
    stock = input('Please enter your symbol: ')
    stock = stock.upper()
    #symbol = plot_bollingerband(stock)
    symbolprice = plot_candlestick(stock)
    print(symbolprice)
    #print(symbol)
    # symbol2 = plot_momentum(stock)
    # print(symbol2)