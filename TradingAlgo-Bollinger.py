##Your manager wants to see if Bollinger Bands are still a meaningful technical analysis strategy on their own. For this exercise, you will be testing Johnson and Johnson sid(4151).Specifically, your manager has decided he wants set 100% of the portfolio to go long when the stock price is below 2 times the 20 day rolling standard deviation subtracted from the 20 day moving average, and go 100% short of the portfolio on that stock when the current price is above 2 times the 20 day rolling standard deviation added on to the 20 day moving average. The check for this signal event should only happen once per day. This is probably a very unreasonable strategy, but the main point of this is to exercise your ability to write out backtest algorithms with Quantopian.


import numpy as np

def initialize(context):
    schedule_function(check_signal,date_rules.every_day())
    
    context.jnj = sid(4151)

    
def check_signal(context,data):
    
    jnj = context.jnj
    
    current_price = data.current(jnj,'price')
    
    prices = data.history(jnj,'price',20,'1d')
    
    avg = prices.mean()
    std = prices.std()
    lower_band = avg - 2*std
    upper_band = avg + 2*std
    
    if current_price <= lower_band:
        order_target_percent(jnj,1)
        print('Long Stock')
        print('Current price is: ' + str(current_price))
        print('Lower band is: ' + str(lower_band))
    
    elif current_price >= upper_band:
        order_target_percent(jnj,-1)
        print('Short Stock')
        print('Current price is: ' + str(current_price))
        print('Upper band is: ' + str(upper_band))
        
    else:
        pass
    
    record(upper=upper_band,lower=lower_band,ma_20=avg,price=current_price)