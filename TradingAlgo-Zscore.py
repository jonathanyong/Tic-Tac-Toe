##This Z-Score algorithm hypothesizes that when 2 stocks deviate too much away from their mean difference, we should sell the overpriced stock and buy the underpriced stock
##as the 2 stocks have a tendency to fall back to its mean difference. When the stocks trading too close to its mean difference, we should close all positions as there is a 
##high chance for the 2 stocks to deviate from the mean, and we do not know which stock will be overpriced, and which will be underpriced. The Z-Score measures the number of 
##standard deviations from the mean data point. It follows a normalized distribution chart.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

### Determine the optimal ZScore ###

# Pulling stock data for given time range
start = '2015-01-01'
end = '2017-01-01'

united = get_pricing('UAL',start_date=start,end_date=end)
american = get_pricing('AAL',start_date=start,end_date=end)

# Calculating the spread of the 2 stocks
spread = american['close_price']-united['close_price']
spread.plot(label='Spread',figsize=(12,8))
plt.axhline(spread.mean(),c='r')

# Normalizing the spread into a ZScore
def zscore(stocks):
    return (stocks-stocks.mean())/np.std(stocks)

# Determining optimal ZScore for the spread
zscore(spread).plot(figsize=(14,8))
plt.axhline(zscore(spread).mean(),c='black')
plt.axhline(1.0,c='g',ls='--')
plt.axhline(-1.0,c='r',ls='--')

# Determining optimal 30 day MA ZScore for the spread
spread_mavg1 = spread.rolling(1).mean()
spread_mavg30 = spread.rolling(30).mean()
std_30 = spread.rolling(30).std()
zscore_30_1 = (spread_mavg1-spread_mavg30)/std_30

zscore_30_1.plot(figsize= (12,8), label='Rolling 30 Day Z Score')
plt.axhline(0,c='black')
plt.axhline(2.0,c='green',ls='--')

### Coding the Trade Algorithm ###

def initialize(context):
    schedule_function(check_pairs,date_rules.every_day(),time_rules.market_close(minutes=60))
    
    context.aa = sid(45971)
    context.ual = sid(28051)
    
    context.long_on_spread = False
    context.shorting_spread = False
# check_pairs
def check_pairs(context,data):
    
    aa = context.aa
    ual = context.ual
    
    prices = data.history([aa,ual],'price',30,'1d')
    
    short_prices = prices.iloc[-1:]
    
    # Spread
    mavg_30 = np.mean(prices[aa] - prices[ual])
    std_30 = np.std(prices[aa] - prices[ual])
    
    mavg_1 = np.mean(short_prices[aa]-short_prices[ual])
    
    if std_30 > 0:
        zscore = (mavg_1 - mavg_30)/std_30
        
        if zscore > 2.0 and not context.shorting_spread:
            #spread = AA - UAL
            order_target_percent(aa,-0.5)
            order_target_percent(ual,0.5)
            context.shorting_spread = True
            context.long_on_spread = False
        
        elif zscore < 2.0 and not context.shorting_spread:
            #spread = UAL - AA
            order_target_percent(aa,0.5)
            order_target_percent(ual,-0.5)
            context.shorting_spread = False
            context.long_on_spread = True
        
        # Close position if zscore is too close to mean
        elif abs(zscore) < 0.1:
            order_target_percent(aa,0)
            order_target_percent(ual,0)       
            context.shorting_spread = False
            context.long_on_spread = False
            
        # Recording the ZScore for the given time horizon
        record(Z_score = zscore)