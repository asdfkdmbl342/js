import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# Streamlit 앱 제목
st.title("Stock Analysis App")

# 사용자로부터 주식 종목과 기간 입력 받기
ticker = st.text_input("Enter stock ticker", "AAPL")
start_date = st.date_input("Start date", value=pd.to_datetime("2022-01-01"))
end_date = st.date_input("End date", value=pd.to_datetime("today"))

# 주식 데이터 가져오기
@st.cache_data
def get_data(ticker, start, end):
    stock_data = yf.download(ticker, start=start, end=end)
    return stock_data

if ticker:
    data = get_data(ticker, start_date, end_date)
    
    # 데이터프레임 표시
    st.subheader(f"{ticker} Stock Data")
    st.dataframe(data)
    
    # 종가 시각화
    st.subheader("Closing Price")
    fig, ax = plt.subplots()
    ax.plot(data.index, data['Close'], label='Close Price')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legend()
    st.pyplot(fig)
    
    # 이동평균선 추가
    st.subheader("Moving Averages")
    data['MA50'] = data['Close'].rolling(50).mean()
    data['MA200'] = data['Close'].rolling(200).mean()
    
    fig, ax = plt.subplots()
    ax.plot(data.index, data['Close'], label='Close Price')
    ax.plot(data.index, data['MA50'], label='50-day MA')
    ax.plot(data.index, data['MA200'], label='200-day MA')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legend()
    st.pyplot(fig)
