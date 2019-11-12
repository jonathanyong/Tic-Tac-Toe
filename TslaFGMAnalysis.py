import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import pandas_datareader
import datetime
import pandas_datareader.data as web

###### Data Import and Visualization ######

#Import Tesla Stock data from Yahoo finance
start = datetime.datetime(2012, 1, 1)
end = datetime.datetime(2017, 1, 1)
Tesla = web.DataReader("TSLA",'yahoo', start, end)

#Import Ford and GM Stock data from Yahoo finance
start = datetime.datetime(2012, 1, 1)
end = datetime.datetime(2017, 1, 1)
Ford = web.DataReader("F",'yahoo', start, end)
GM = web.DataReader("GM",'yahoo', start, end)

#Save imported data to CSV
Tesla.to_csv('Tesla_Stock.csv')
Ford.to_csv('Ford_Stock.csv')
GM.to_csv('GM_Stock.csv')

#Visualize daily open price for 3 stocks
Tesla['Open'].plot(label='Tesla',figsize=(16,8),title='Open Price')
Ford['Open'].plot(label='Ford')
GM['Open'].plot(label='GM')
plt.legend()

#Visualize daily volume traded for 3 stocks
Tesla['Volume'].plot(label='Tesla',figsize=(16,8),title='Volume Traded')
Ford['Volume'].plot(label='Ford')
GM['Volume'].plot(label='GM')
plt.legend()

#Find the day in which Ford has the highest trading volume
Ford['Volume'].argmax()

#Creating a new column Total Traded
Tesla['Total Traded']=Tesla['Volume']*Tesla['Open']
Ford['Total Traded']=Ford['Volume']*Ford['Open']
GM['Total Traded']=GM['Volume']*GM['Open']

#Visualize daily Total Traded for 3 stocks
Tesla['Total Traded'].plot(label='Tesla',figsize=(16,8))
Ford['Total Traded'].plot(label='Ford')
GM['Total Traded'].plot(label='GM')
plt.legend()
plt.ylabel('Total Traded')

#Find the day in which Tesla has the highest Total Traded
Tesla['Total Traded'].argmax()

#Plotting 50MA and 200MA for GM stock
GM['MA50']=GM['Open'].rolling(50).mean()
GM['MA200']=GM['Open'].rolling(200).mean()
GM[['Open','MA50','MA200']].plot(label='GM',figsize=(16,8))

#Plot scatter_matrix for the 3 stocks to compare their relationship
from pandas.plotting import scatter_matrix
car_comp = pd.concat([Tesla['Open'],Ford['Open'],GM['Open']],axis = 1)
car_comp.columns = ['Tesla Open','Ford Open','GM Open']
scatter_matrix(car_comp,figsize = (8,8),alpha = 0.4,hist_kwds={'bins':50});

#Plot a candlestick graph for Ford stock
from matplotlib.dates import DateFormatter, WeekdayLocator,DayLocator, MONDAY, date2num
from mpl_finance import candlestick_ohlc
ford_reset = Ford.loc['2012-01':'2012-01'].reset_index()
ford_reset['date_ax']=ford_reset['Date'].apply(lambda date: date2num(date))
ford_values = [tuple(vals) for vals in ford_reset[['date_ax','Open','High','Low','Close']].values]
mondays = WeekdayLocator(MONDAY)
alldays = DayLocator()
weekFormatter = DateFormatter('%b %d')
dayFormatter = DateFormatter('%d')
fig,ax=plt.subplots()
fig.subplots_adjust(bottom = 0.2)
ax.xaxis.set_major_locator(mondays)
ax.xaxis.set_minor_locator(alldays)
ax.xaxis.set_major_formatter(weekFormatter)
candlestick_ohlc(ax, ford_values, width=0.6, colorup='g',colordown='r');

###### Financial Analysis ######

#Creating a Returns column for all 3 stocks and returning results
Tesla['Returns'] = (Tesla['Close']/Tesla['Close'].shift(1))-1
Tesla['Returns'] = Tesla['Close'].pct_change(1)
Ford['Returns'] = Ford['Close'].pct_change(1)
GM['Returns'] = GM['Close'].pct_change(1)
Tesla.head()
Ford.head()
GM.head()

#Plotting a histogram for 3 stocks
Tesla['Returns'].hist(bins=100,figsize=(10,8),label = 'Tesla',alpha=0.4)
Ford['Returns'].hist(bins=100,label='Ford',alpha=0.4)
GM['Returns'].hist(bins=100,label='GM',alpha=0.4)
plt.legend()

#Plotting a kde for 3 stocks
Tesla['Returns'].plot(kind ='kde',figsize=(16,8),label = 'Tesla',alpha=0.4)
Ford['Returns'].plot(kind='kde',alpha=0.4)
GM['Returns'].plot(kind='kde',label='GM',alpha=0.4)
plt.legend()

#Plotting a boxplot for 3 stocks
box_df = pd.concat([Tesla['Returns'],Ford['Returns'],GM['Returns']],axis=1)
box_df.columns = ['Tesla Returns','Ford Returns','GM Returns']
box_df.plot(kind='box',figsize=(8,11))

#Comparing results of all 3 stock returns
scatter_matrix(box_df,figsize = (8,8),alpha = 0.4,hist_kwds={'bins':50});

#Determining relationship between Ford and GM
box_df.plot(kind='scatter',x='Ford Returns',y='GM Returns',figsize = (8,8),alpha = 0.4)

#Creating culumative daily return column for 3 stocks
Tesla['Cumulative Daily Return']=(1+Tesla['Returns']).cumprod()
Ford['Cumulative Daily Return']=(1+Ford['Returns']).cumprod()
GM['Cumulative Daily Return']=(1+GM['Returns']).cumprod()

#Visualizing cumulative daily return for 3 stocks
Tesla['Cumulative Daily Return'].plot(label='Tesla',figsize=(16,8),title='Cumulative Return')
Ford['Cumulative Daily Return'].plot(label='Ford')
GM['Cumulative Daily Return'].plot(label='GM')
plt.legend()