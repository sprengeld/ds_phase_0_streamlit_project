import yfinance as yf
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mplfinance.original_flavor import candlestick_ohlc
import seaborn as sns
import warnings

warnings.filterwarnings(
    "ignore"
)  # отключение предупреждений в терминале по мере написания кода

# Название
st.title("Котировки компании Apple")

# Описание
st.write(
    "На странице представлены данные о котировках компании Apple за период **01.01.2015-31.12.2024**"
)

# Основной код
# тикер для компании Apple
tickerSymbol = "AAPL"
# получение данных по тикеру
tickerData = yf.Ticker(tickerSymbol)
# извлечение данных об измении котировок в определенный период
tickerDf = tickerData.history(start="2015-01-01", end="2024-12-31")
# Open, High, Low, Close, Volume, Dividends, Stock Splits

st.write(
    """
###  Цена закрытия
Последняя цена акции в конце торгового периода
         """
)
st.line_chart(tickerDf["Close"])

st.write(
    """
###  Объем торгов
Количество проданных/купленных акций за период
         """
)
st.line_chart(tickerDf["Volume"])

st.subheader("Анализ торговой активности на финансовом рынке за декабрь 2024")
# Подготовка данных
data_candle = tickerData.history(start="2024-12-01", end="2024-12-31")
data_candle.reset_index(inplace=True)
data_candle["Date"] = data_candle["Date"].map(mdates.date2num)
# свечной график
fig, ax = plt.subplots()
candlestick_ohlc(
    ax,
    data_candle[["Date", "Open", "High", "Low", "Close"]].values,
    width=0.6,
    colorup="g",
    colordown="r",
)
ax.xaxis_date()
ax.xaxis.set_major_formatter(mdates.DateFormatter("%d.%m"))
ax.set_ylabel("Цена, $")
ax.set_title("Свечной график Apple (AAPL)")
ax.grid(True, alpha=0.3)
st.pyplot(fig)

st.write(
    """
###  Максимум и минимум
Самая высокая / низкая цена акции в декабре 2024
         """
)
fig, ax = plt.subplots()
ax.plot(data_candle["Date"], data_candle["Low"], label="Минимум")
ax.plot(data_candle["Date"], data_candle["High"], label="Максимум")
ax.xaxis_date()
ax.xaxis.set_major_formatter(mdates.DateFormatter("%d.%m"))
ax.set_ylabel("Цена, $", labelpad=6)
ax.legend(loc="upper left", ncol=2)
ax.grid(True, alpha=0.3)
st.pyplot(fig)
