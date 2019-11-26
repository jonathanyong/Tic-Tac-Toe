from quantopian.pipeline import Pipeline
from quantopian.pipeline.data.sentdex import sentiment
from quantopian.pipeline.domain import US_EQUITIES
from quantopian.pipeline.factors import SimpleMovingAverage
from quantopian.pipeline.filters.morningstar import Q1500US
from quantopian.algorithm import attach_pipeline,pipeline_output

def initialize(context):
    schedule_function(my_rebalance,date_rules.every_day(),time_rules.market_open())
    
    attach_pipeline(make_pipeline(),'my_pipeline')

def my_rebalance(context,data):
    for security in context.longs:
        order_target_percent(security,0.01)
    
    for security in context.shorts:
        order_target_percent(security,-0.01)

def before_trading_start(context,data):
    context.output = pipeline_output('my_pipeline')
    
    # Long
    context.longs = context.output[context.output['longs']].index.tolist()    
    
    # Short
    context.shorts = context.output[context.output['shorts']].index.tolist()    
    
def make_pipeline():
    # Sentiment Analysis
    sentiment_factor = sentiment.sentiment_signal.latest
    universe = (Q1500US() & sentiment_factor.notnull())
    
    # Longs
    longs = sentiment_factor >= 4
    
    # Shorts
    shorts = sentiment_factor <= -2