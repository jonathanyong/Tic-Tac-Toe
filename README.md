# Tic-Tac-Toe
First Milestone project completed from Udemy: Complete Python Bootcamp course - Jose Portilla

# BlackJack
Second Milestone project completed from Udemy: Complete Python Bootcamp course - Jose Portilla

# TslaFGMAnalysis
Third Milestone project completed from Udemy: Python for Financial Analysis and Algorithmic Trading - Jose Portilla

Embarking on this third milestone project taught me more about visualization techniques and tools using pandas, matplotlib, pandas_datareader, and pulling data from online sources such as yahoo finance. This project taught me more about Quandl as a company and the different financial data API that can be attained from their website. These data are valuable in financial analysis, and greatly value-adds to coders out there. 

However, there were some roadblocks along the way, such as google changing its API, matplotlib.finance having changed its API to mpl_finance instead, not understanding what candlestick_ohlc actually means, not understanding what date2num from matplotlib.dates actually does, as well as understanding how to calculate cumulative daily return using .cumprod(). There are 2 issues which I felt could be improved on, including the difference in code for plotting a histogram vs. plotting a kde graph. A histogram plot code e.g. Tesla['Volume'].hist() , while a kde is Tesla['Volume'].plot(kind='kde') instead of Tesla['Volume'].kde(). The other issue would be that why do we need to concatenate data when plotting a boxplot but not a histogram or kde? It was a challenge trying to apply what was taught in the matplotlib lectures on changing datalabels, formatting datetime indexes into non-datetime etc. 

Overall, I felt that learning the basics of financial analysis using python and data visualization will be much helpful in pursuing much in-depth financial analysis. 

Investment analysts today still rely heavily on spreadsheets to do their financial modelling etc, which makes me wonder whether it is possible (and easier) to conduct financial analysis methods (e.g. DCF) using python? Has anyone produced a fintech product which could automatically generate a DCF model and its results just by importing a PDF file? At the back of my mind, I believe that there will be alot of junk data and noise data which hinders the ease of making analysis automated today, hence the need for what they call a "Data Analyst" to clean up the data.

# TradingAlgo-Zscore
This Z-Score algorithm hypothesizes that when 2 stocks deviate too much away from their mean difference, we should sell the overpriced stock and buy the underpriced stock as the 2 stocks have a tendency to fall back to its mean difference. When the stocks trading too close to its mean difference, we should close all positions as there is a high chance for the 2 stocks to deviate from the mean, and we do not know which stock will be overpriced, and which will be underpriced. The Z-Score measures the number of standard deviations from the mean data point. It follows a normalized distribution chart.

My first trading algorithm taught me alot about pulling data and coding using quantopian. Things I have learnt in this exercise include initializing a trade, defining parameters for the trade, in this case the Z-Score, recording any data we want of the trade (Z-Score), as well as determining the optimal z-score to open and close a trade, using historical data. 

The flaws of this algorithm is that the 30 day Moving average Z-Score is still a lagging indicator, and may not be predictive of the future performance of the 2 stocks. We are still unable to accurately determine the support and resistance of the Z-Score to open a trade, and hence for now have to depend on the manual process of plotting the historical data, plotting the chart and observing the chart manually.

Results (4 Years backtest from 7/4/2015 - 19/11/2019):
Returns = -24.63%
Beta = 0.10
Sharpe = -0.52
Drawdown = -42.71%
From the chart, the algorithm works best in 2016 and started to give declining results from 2017 onwards, erasing profits from September 2017 onwards. It has the worst performance in 2018 and 2019.

# TradingAlgo-Bollinger
The bollinger band in this algorithm is set to 2 standard deviations away from a 20 day MA for the selected stock Johnson & Johnson. The algorithm purchases 100% of portfolio into the stock when the current price of the stock is below the lower bound, or shorts 100% of portfolio of the stock when the current price of the stock is above the upper bound.

Just like the algorithm in TradingAlgo-Zscore, the bollinger algorithm is also a lagging indicator and is not indicative of future performance. Using a single indicator as trading strategy is insufficient to generate consistently profitable results.

Results (5 Years backtest from 19/11/2014 - 10/11/2019):
Returns = 19.6%
Beta = 0
Sharpe = 0.28
Drawdown = -22.1%
From the chart, the algorithm saw a sharp spike in returns at the end of 2015 and was on a gradual downhill ever since. This may be because there was no revision / close positions being formulated in the algorithm itself, hence the portfolio did not rebalance after a 100% buy in at the end of 2015. The performance of the portfolio hence followed the performance of the stock itself.
