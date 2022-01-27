#ROI section:
import numpy as np
import pandas as pd
import vnquant.DataLoader as dl
from datetime import datetime

class SimpleForcast:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_data(self):
        start = '2021-01-01'
        now = datetime.now()
        end = now.strftime("%Y-%m-%d")
        loader = dl.DataLoader(self.symbol, start, end, data_source='VND', minimal=True)
        data = loader.download()
        close_data = data['close'].dropna()

        self.historical_data = pd.DataFrame(close_data)
        return self.historical_data

    def calculate_ROI(self):
        data = self.historical_data.copy().dropna()
        initial_investment = -1000000000

        symbol_string = data[self.symbol]
        price = []
        for i in symbol_string:
            price.append(i)

        number_of_stock = round(-initial_investment / (price[0] * 1000), -2)

        ROI = (price[-1] * number_of_stock -
               (price[0] * number_of_stock)) / (number_of_stock * price[0])
        ROI = round(ROI, 2)
        ROI = "{:.0%}".format(ROI)
        string = f'The ROI for {self.symbol} (2021 only) is: '
        final = string + ROI
        return final

    def calculate_PE(self):
        start = '2019-01-01'
        now = datetime.now()
        end = now.strftime("%Y-%m-%d")

        #take the EPS
        loader2 = dl.FinanceLoader(self.symbol, start, end, data_source='VND', minimal=True)
        data_bus = loader2.get_business_report()
        latestEPS = sum(data_bus.loc['Lãi cơ bản trên cổ phiếu'][:4])
        #take the price
        loader = dl.DataLoader(self.symbol, start, end, data_source='VND', minimal=True)
        data = loader.download()
        close_data = data['close'].dropna()


        # print(type(latestEPS))
        #latestEPS = latestEPS.item()
        # print(type(latestEPS))
        resultEPS = str(latestEPS)


        # calculate PE
        priceDataframe = pd.DataFrame(close_data)
        latestPrice = priceDataframe[self.symbol][-1] *1000
        PE = round(latestPrice/latestEPS,1)
        PE_string = str(PE)
        string = f'The PE for {self.symbol} is: '
        final = string + PE_string  # concatenate the EPS statement
        return final


if __name__ == '__main__':
    VHM = SimpleForcast('VHM')
    VHM.get_data()
    print(VHM.calculate_ROI())
    VND  = SimpleForcast('SSI')
    PE = VND.calculate_PE()
    print(PE)
