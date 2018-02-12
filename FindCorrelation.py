import pandas as pd
import numpy as np
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import datetime

def find_max_correlation_index_ticker(corr_for_ticker):
    max_corr = -1.0
    max_corr_index = ""
    for key,value in corr_for_ticker.items():
        if(value >= max_corr):
            max_corr = value
            max_corr_index = key
    return max_corr_index


def get_data(index_ticker):
    while True:
        try:
         df = web.DataReader(index_ticker, 'yahoo', start_date, end_date)
        except:
            continue
        break
    return df
#
# ticker_df = web.DataReader('IBM', 'yahoo', start_date, end_date)
# index_df = web.DataReader('^IXIC', 'yahoo', start_date, end_date)
# value = index_df['Adj Close'].corr(ticker_df['Adj Close'])
# print(value)
#

ticker_list=['IBM', 'MSFT', 'ORCL', 'CSCO', 'XOM']
index_ticker = ['^IXIC','^NYA','^DJI','^GSPC','000001.SS','^STOXX50E']

end_date = datetime.datetime.now()
start_date = end_date - datetime.timedelta(2*365)

#
# df = web.DataReader(index_ticker[0], 'yahoo', start_date, end_date)
# # print("Data contains {} rows and {} columns".format(*df.shape))
# print(df['Adj Close'].head())

max_corr_ticker_index = {}
for ticker in ticker_list:
    ticker_df = get_data(ticker) #web.DataReader(ticker, 'yahoo', start_date, end_date)
    corr_for_ticker = {}
    for index in index_ticker:
        index_df = get_data(index)#web.DataReader(index, 'yahoo', start_date, end_date)
        value = index_df['Adj Close'].pct_change().corr(ticker_df['Adj Close'].pct_change())
        corr_for_ticker[index] = value
    max_corr_ticker_index[ticker] = find_max_correlation_index_ticker(corr_for_ticker)
print(max_corr_ticker_index)


max_corr_index_ticker = {}
for index in index_ticker:
    index_df = get_data(index) #web.DataReader(ticker, 'yahoo', start_date, end_date)
    corr_for_index = {}
    for ticker in ticker_list:
        ticker_df = get_data(ticker)#web.DataReader(index, 'yahoo', start_date, end_date)
        value = ticker_df['Adj Close'].pct_change().corr(index_df['Adj Close'].pct_change())
        corr_for_index[ticker] = value
    max_corr_index_ticker[index] = find_max_correlation_index_ticker(corr_for_index)
print(max_corr_index_ticker)



