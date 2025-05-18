import yfinance as yf
import pandas as pd

def get_stock_data(symbol="TSLA", period="6mo", interval="1d"):
    stock = yf.Ticker(symbol)
    df = stock.history(period=period, interval=interval)
    df.reset_index(inplace=True)
    return df

def add_sma(df, window=14):
    df[f'SMA_{window}'] = df['Close'].rolling(window=window).mean()
    return df

def calculate_rsi(df, period=14):
    delta = df['Close'].diff()
    gain = delta.clip(lower=0).rolling(window=period).mean()
    loss = -delta.clip(upper=0).rolling(window=period).mean()
    rs = gain / loss
    df['RSI'] = 100 - (100 / (1 + rs))
    return df
