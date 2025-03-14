# import pandas as pd
# dict_ = {'a':[11, 21, 31], 'b':[12, 22, 32]}
# df = pd.DataFrame(dict_)

# df.head()
# df.mean()
from pycoingecko import CoinGeckoAPI
import pandas as pd
import plotly.graph_objects as go

# def fetch_crypto_data(coin_id='bitcoin', vs_currency = 'usd', days=30):
#     #gets information from coingecko
#     try:
#         cg = CoinGeckoAPI()
#         data = cg.get_coin_market_chart_by_id(id=coin_id, vs_currency=vs_currency, days=days)
#         return data['prices']
#     except Exception as e:
#         print(f"⚠️ ERROR: Data couldn't get from API! ({e})")
#         return None
    
# def process_data(price_data):
#     """Taken data transformed by Pandas to DataFrame and TimeStamps transformed to date time."""
#     if price_data is None:
#         return None
    
#     df = pd.DataFrame(price_data, columns=['TimeStamps', 'Price'])
#     df['Date'] = pd.to_datetime(df['TimeStamps'], unit='ms')

#     # Calculation of #min #max #first and #last
#     candlestick_data = df.resample('D', on='Date').agg({'Price': ['min', 'max', 'first', 'last']})

#     return candlestick_data

# def plot_candlestick_chart(candlestick_data, coin_name="Bitcoin"):
#     """Makes candlestick graph"""
#     if candlestick_data is None or candlestick_data.empty:
#         print("⚠️ Warning: You don't have enough data to make chart!")
#         return
    
#     fig = go.Figure(data=[go.Candlestick(
#         x=candlestick_data.index,
#         open=candlestick_data['Price']['first'],
#         high=candlestick_data['Price']['max'],
#         low=candlestick_data['Price']['min'],
#         close=candlestick_data['Price']['last']
#     )])

#     fig.update_layout(
#         xaxis_rangeslider_visible=False,
#         xaxis_title="Day",
#         yaxis_title="Price ($USD)",
#         title=f"{coin_name} Candlestick Graph (Last {len(candlestick_data)} Day)"
#     )

#     fig.show()


# COIN_ID = 'bitcoin'  
# VS_CURRENCY = 'usd'
# DAYS = 30 

# #graphic draw
# price_data = fetch_crypto_data(coin_id=COIN_ID, vs_currency=VS_CURRENCY, days=DAYS)
# candlestick_data = process_data(price_data)
# plot_candlestick_chart(candlestick_data, coin_name=COIN_ID.capitalize())


#take bitcoin price data from coingeckoapi
cg = CoinGeckoAPI()
bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days=30)

#data transforms to dataframe
data = pd.DataFrame(bitcoin_data['prices'], columns=['TimeStamps', 'Price'])

#unix timestamps transforms to date format
data['Date'] = pd.to_datetime(data['TimeStamps'], unit='ms')

#make data groups
candlestick_data = data.groupby(data.Date.dt.date).agg({
    'Price': ['min', 'max', 'first', 'last']
})

#candlestick configurations
plotlyfig = go.Figure(data=[go.Candlestick(
    x=candlestick_data.index,
    open=candlestick_data['Price']['first'],
    high=candlestick_data['Price']['max'],
    low=candlestick_data['Price']['min'],
    close=candlestick_data['Price']['last']
)])

#graphic updates
plotlyfig.update_layout(
    xaxis_rangeselector_visible=False, 
    xaxis_title='Date', 
    yaxis_title='Price ($USD)', 
    title='Bitcoin Candlestick Chart Over Past 30 Days'
)


plotlyfig.show()
