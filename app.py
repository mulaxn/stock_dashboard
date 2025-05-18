import streamlit as st
import plotly.graph_objs as go
from stock_utils import get_stock_data, add_sma, calculate_rsi

st.set_page_config(page_title="StockView", layout="wide")
st.title("📈 StockView: A Real-Time Market Dashboard")

symbol = st.text_input("Enter Stock Symbol (e.g., AAPL, TSLA):", "TSLA")

if symbol:
    try:
        df = get_stock_data(symbol)
        df = add_sma(df, 7)
        df = add_sma(df, 14)
        df = calculate_rsi(df)

        st.subheader(f"📉 {symbol.upper()} Price Chart")
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df['Date'], y=df['Close'], mode='lines', name='Close Price'))
        fig.add_trace(go.Scatter(x=df['Date'], y=df['SMA_7'], mode='lines', name='SMA 7'))
        fig.add_trace(go.Scatter(x=df['Date'], y=df['SMA_14'], mode='lines', name='SMA 14'))
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("📊 RSI Indicator")
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=df['Date'], y=df['RSI'], mode='lines', name='RSI'))
        fig2.update_yaxes(range=[0, 100])
        st.plotly_chart(fig2, use_container_width=True)

        st.subheader("📅 Recent Data")
        st.dataframe(df.tail())

    except Exception as e:
        st.error(f"Error fetching or displaying data: {e}")
