"""
Name: Esuabom Dijemeni
Date: 25/08/2018
Purpose: reading and analysing stock data
"""
#Imported libraries
import pandas as pd

# Read the input data
"""
with open('prices.csv','r')as file:
    prices = file.read()

print(prices)
"""

# Read input data as a data frame
price_df = pd.read_csv('prices.csv', names=['ticker', 'date','open','high','low',
                                                'close','volume','adj_close','adj_volume'])

print(price_df)

# Median value
# print(price_df.groupby('ticker').median())

# Data selection
# print(price_df.iloc[[6,7,13,14]])

# Dataframe pivot
open_prices = price_df.pivot(index='date', columns='ticker', values='open')
high_prices = price_df.pivot(index='date', columns='ticker', values='high')
low_prices = price_df.pivot(index='date', columns='ticker', values='low')
close_prices = price_df.pivot(index='date', columns='ticker', values='close')
volume = price_df.pivot(index='date', columns='ticker', values='volume')
adj_close_prices = price_df.pivot(index='date', columns='ticker', values='adj_close')
adj_volume = price_df.pivot(index='date', columns='ticker', values='adj_volume')

'''
print(open_prices)
print(high_prices)
print(low_prices)
print(close_prices)
print(volume)
print(adj_close_prices)
print(adj_volume)
'''
print(open_prices.mean())

print(open_prices.T.mean())
