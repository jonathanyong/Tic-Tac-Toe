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

# SentdexSentiment
Spent the past few days learning about sentiment analysis and how it can possibly be implemented into trading algorithms. Quantopian platform has a sentdex sentiment anlaysis package in its pipeline data which analyzes news from sources such as bloomberg, CNBC etc. which analyzes news sentiments and ranks them from a -3 to 6. The accuracy of this package is, I believe, about 80% or so today.

This file is just a basic execution code for analyzing Q1500US stocks and determining its sentiment factor, before shorting stocks with <=-2 in sentiment factor and entering into a long for those with a sentiment factor of >=4. It is a very simple implementation of the code and will probably require much more in-depth optimization before implementing it to an actual trading algorithm. I am not too sure, but I believe that sentdex sentiment analysis is coded on the basis of naive bayes theorem.

Apart from sentdex sentiment analysis, there are other sentment analysis packages available in the open source, as well as premium models today, for example VADER sentiment analysis which is primarily used for social media text recognition and sentiment analysis. The links to the two packages are attached below for reference.

Sentdex Social Sentiment: https://github.com/Sentdex/ | socialsentiment.net
Sentdex market sentiment: http://sentdex.com/financial-analysis/?i=SP500&tf=7d
Vader Sentiment: https://github.com/cjhutto/vaderSentiment

The Sentdex market sentiment is good enough for building the trading algorithm, hence there is no need to code sentiment analysis packages again. However, the next step is still to implement the sentdex sentiment class into a trading algorithm and optimize its trading results.

# opentabledata
Diving into techincal books, I chanced on a very good book that teaches on how to do algorithmic trading using machine learning, written by Stefan Jansen. This file is a hands-on practice of chapter 3 of the book, where he teaches how to retrieve HTML data using requests, BeautifulSoup, Selenium, Scrapy and splash, building a dataset of restaurant bookings from the website https://www.opentable.com/. The key differences and uses are as follows:

requests: pull data from website html
BeautifulSoup: Parses pulled data after using requests. Unable to read JavaScript files
Selenium: Enables automation of HTML data parsing, and creating a code that allows selenium to click 'Next' for us and parse data until the end. So it works like a bot.
Scrapy: Crawls through the given website
Splash: Parses the data and stores it in a structured way e.g. css file

This chapter required the understanding of geckodriver and linking webdriver from the selenium package to its correct path. When executing the autobot using selenium, the bot stopped jumping pages after the second, giving an ElementClickInterceptedException error. Upon investigation, there was a line in the code 'sleep(1)' that could not be defined at first, so I removed it. However, the time delay is necessary to allow the animation in the website (probably advertisements) to load, before the bot can skip pages. So, instead of using sleep(1), import time, and use time.sleep(1) instead. The bot will then be able to skip pages automatically.

Now that we know how to draw HTML data from websites and parse it using a bot, this will be useful in machine learning sentiment analysis which I can't wait to learn about in the upcoming chapters of the book.

# EarningsCall
Chapter 3 of Stefan Jansen's book teaches how to retrieve earnings call transcripts of companies from seekingalpha.com, creating a bot that parses through the strings to retrieve specific data such as company name, participants of the selected earnings call transcripts. We then store the data in a CSV file for use in machine learning or analysis in future. 

While coding, I came across error messages such as NoneType error for BeautifulSoup.find. Upon investigation, some of the earnings call transcripts may not exactly contain certain contents we are looking for and hence hinders the bot from continuing to retrieve data. Hence, there is a need to extend the code by adding an if none call, to command the bot to continue running through the code if there is no data. The updated code can be found on Stefan's repository at this link: https://github.com/PacktPublishing/Hands-On-Machine-Learning-for-Algorithmic-Trading/blob/master/Chapter03/02_earnings_calls/sa_selenium.py

Being able to sieve out important data and storing them into CSV format is the first step to creating our machine learning model which I will be diving to subsequently.

# HDF5Format
Chapter 2 of Stefan Jansen's book teaches how to store data into a HDF5 format after retrieving the data and parsing through it. The benefits of storing data into a HDF5 format includes:
1) Storing data into HDF5 format allows for access time and storage space optimizations. 
2) The HDF5 is a versatile data model that represents very complex data objects and a wide range of metadata
3) The file is completely portable with no limit on data size or objects
However, using HDF5 files require special programs such as Java, Python, C++ etc. Only programmers with special training in such languages will be able to use the data stored in these files.

This file shows how historical price data of 3000 US companies from before 27 March 2018 is retrieved from Quandl, then parsed and stored into the HDF5 file 'assets.h5', with columns 'date', 'ticker', 'adj_close', 'split_ratio', 'ex-dividend'. While attempting to learn about storing files into HDF5, the key difficulty i faced was recognizing my Path. In this file, I have added a code that allows you to recognize where your path is.
