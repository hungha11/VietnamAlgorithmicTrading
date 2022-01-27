import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import vnquant.DataLoader as dl
from vnquant import  Plot
from datetime import datetime
from scipy.optimize import brute
import matplotlib.pyplot as plt
from Forecast.SMA_backtesting import SMAVectorBacktester
from Forecast.FUNDAMENTAL_calculation import SimpleForcast
import streamlit as st
from Ploting_price.PlotPrice1y import plot_price_1y_class
















if __name__ =='__main__':
    # streamlit section
    # streamlit is web host for data project, with a few line of code, people can easily deploy
    # a app into web.
    '''
    #       Vietnam Algorithmic trading 
    '''


    # st.write('Algorithmic trading for Vietnam stock market (VN30 only)')
    page = st.sidebar.selectbox('Choose a page', ['Home', 'Portfolio', 'Forecast', 'Result'])

    #                                                   Home
    if page == 'Home':
        st.title('Homepage')

        st.write('Vietnam is a frontier market. In 2021, Vietnam had the highest return compared to others.')
        st.write("Although there's still a lack in the data (due to different IPO date from the companies) , "
                 " this project is still tempting to apply machine into trading activity.")
        #st.write('The project only executes for the VN30 or VN100 index.')
        st.write(""" ***""")
        image = Image.open('/Users/haquochung/OneDrive/OneDrive - RMIT University/Home/PyCharm/VietnamAlgorithmicTrading/streamlit/vietnam-stock-market-graph-business-ho-chi-minh-stock-index-trading-and-analysis-investment-financial-board-display-double-exposure-money-price-stoc-2AB1HBP.jpeg')
        st.image(image, use_column_width=True)
        st.write(""" ***""")





        st.sidebar.write(""" ***""")
        st.sidebar.write('Algorithmic trading is the best combination of data science and finance!')






    #                                                   Portfolio_____________________________________________
    if page == 'Portfolio':
        st.title("Portfolio")
        #main page
        #st.write('This is portfolio allocation')
        with st.expander("Idea"):
            st.write("""
            Kelly criterion\n
            Kelly criterion was first use in gambling for optimize size per bet in order to win in the long run or, should you make the bet.
            With the same idea, trader believe in the suitable size per trade to reach the long term performance. With the expected return over a long period, the the varience and the internal rate of return of the stock over 1 year. 
            """)


        #sidebar
        st.sidebar.write("""***""")
        st.sidebar.write("There are many tactics when it comes to portfolio allocation. This project provide you with: (on the go, not found yet)   : )"
                         "")


    #                                                   Forecast______________________________________________________

    if page == 'Forecast':
        #mainpage
        st.title('Forecasting and Backtesting')
        st.write('The index VN30 or VN100 is also available.')
        with st.expander("Description"):
            st.write("""
            ROI\n
            ROI (Return on Investment) is a simple and provide investor the overview of the performance of the particular stock in a timeframe (1 year for example)""")
            st.write("""***""")
            st.write("""
                        SMA\n
                        There are a "fast" line and a "slow" line when it comes to this strategy. 
                        The fast line is made of the mean of a particular numbers of days (usually <52 days)
                        The slow line is made of the mean of a longer timeframe (252 for example). \n
                        When the fast line cross over the slow line, that's the signal of a bull trend.
                        On the other hand, if the fast line cross down the slow line, that's the signal of bear trend.
                        """)
            st.write("""***""")
            st.write(""" 
            Momentum\n
            Momentum trader believes in the continual trend of a particular stock. 
            If a stock is doing well (go up), it will continue that trend.  
            
            
            """)
        st.write("""***""")
        ticker = st.text_input('Please enter the stock you want to forecast: ')


        #Capitalize the symbol
        if ticker.islower() == True:
            ticker = ticker.upper()




        ##Calculate ROI for stock
        if ticker == '':
            st.write('Please enter a symbol')
        elif ticker == 'VN30':
            stocks = pd.read_csv('/Users/haquochung/OneDrive/OneDrive - RMIT University/Home/PyCharm/MomentumStrategy/Data/VN30.csv')
            symbol_groups = list(stocks['Ticker'])
            symbol_strings = []
            for i in range(0, len(symbol_groups)):
                symbol_strings.append(symbol_groups[i])

            for name in symbol_strings:

                company = SimpleForcast(name)
                company.get_data()
                output = company.calculate_ROI()
                st.write(output)
                PE = company.calculate_PE()
                st.write(PE)
        elif ticker == 'VN100':
            stocks = pd.read_csv('/Users/haquochung/OneDrive/OneDrive - RMIT University/Home/PyCharm/Vietnam quant/streamlit/Data/VN100.csv')
            symbol_groups = list(stocks['Ticker'])
            symbol_strings = []
            for i in range(0, len(symbol_groups)):
                symbol_strings.append(symbol_groups[i])

            for name in symbol_strings:
                company = SimpleForcast(name)
                company.get_data()
                output = company.calculate_ROI()
                st.write(output)
                PE = company.calculate_PE()
                st.write(PE)
        else:
            company = SimpleForcast(ticker)
            company.get_data()
            output = company.calculate_ROI()
            st.write(output)
            PE = company.calculate_PE()
            st.write(PE)

        st.write('PE of many companies are still missing. \n'
                 'Therefore, PE is just for fun : ).')





        #sidebar
        st.sidebar.write("""***""")
        st.sidebar.write('There are a lot of techniques which can be used for forecasting.')
        st.sidebar.write('One of them are using past performance.')
        st.sidebar.write('This project will use ROI, and backtesting strategy of SMA and Momentum.')

        ##Backtesting
        st.write("""***""")
        if ticker:
            @st.cache
            def plot_the_price(symbol):
                target = plot_price_1y_class(symbol)
                target.get_data_1y()
                figure = target.plot_candle_1y()


            plot_the_price(ticker)
            st.pyplot()


        #This function is quite good, however, when plotting it not sufficient'''
            # @st.cache
            # def plot_the_price(ticker):
            #
            #     now = datetime.now()
            #     end = now.strftime("%Y-%m-%d")
            #     Plot._vnquant_candle_stick(data=ticker,
            #                            title=f'{ticker} stock price data and volume from 2021-01-01 to now',
            #                            xlab='Date', ylab='Price',
            #                            start_date='2021-01-01',
            #                            end_date=end,
            #                            show_vol=True)
            #plot_the_price(ticker)









        if ticker:
            

            st.subheader('SMA backtesting strategy')
            fast_sma = st.number_input('Chose the timeframe for fast line (> 1) :', min_value=1, max_value=52)
            fast_sma = int(fast_sma)
            slow_sma = st.number_input('Chose the timeframe for slow line (> 22):', min_value=22, max_value=252)
            slow_sma = int(slow_sma)

            if fast_sma:
                smabt = SMAVectorBacktester(ticker, fast_sma, slow_sma, '2019-01-01', '2021-01-01')
                st.set_option('deprecation.showPyplotGlobalUse', False)
                st.write(smabt.run_strategy())
                smabt.plot_results()
                st.pyplot()
                if st.button('Optimizing the input'):
                    st.write('Optimizing.....')
                    smabt.optimization_parameters((30,56,4),(200,300,4))
                    smabt.plot_results()
                    st.pyplot()
                    if st.button('Close'):
                        st.write('Other symbols?')


        st.write("""***""")


    #                                                   Result________________________________________________________

    if page == 'Result':

        #mainpage
        st.title('Result')
        st.write('Still thinking what will be in here. May be the summary of the portfolio and forecast past')





        #sidebar
        st.sidebar.write('Some thing about my self: \n'
                         '* I study at RMIT Vietnam university with the major in Finance.\n'
                         '* My biggest teacher of this field is Youtube : ), especially freeCodeCamp channel!. Everyone should take a look because it do helo you guys!\n'
                         '* There are lots of bug in this project and I am really happy if you guys can find out then contact me!')
        st.sidebar.write(("""***"""))

        st.sidebar.write('Contact: \n'
                         '* Email: qhung9621@gmail.com')


