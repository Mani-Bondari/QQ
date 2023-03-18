import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import talib
import yfinance as yf

symbol = 'AAPL'
start_date = '2010-01-01'
end_date = '2022-03-18'

data = yf.download(symbol, start=start_date, end=end_date)

data['macd'], data['macdsignal'], data['macdhist'] = talib.MACD(data['Close'])
data['rsi'] = talib.RSI(data['Close'])

fig, ax = plt.subplots(figsize=(12, 8))

data['Close'].plot(ax=ax)
ax.set_ylabel('Price')

ax2 = ax.twinx()

data['macd'].plot(ax=ax2, color='blue', label='MACD')
data['macdsignal'].plot(ax=ax2, color='red', label='Signal')
data['macdhist'].plot(ax=ax2, color='green', label='Histogram')
ax2.set_ylabel('MACD')

data['rsi'].plot(ax=ax2, color='purple', label='RSI')
ax2.axhline(30, color='gray', linestyle='--')
ax2.axhline(70, color='gray', linestyle='--')
ax2.set_ylim(0, 100)

lines, labels = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper left')

plt.show()

data['macd'], data['macdsignal'], data['macdhist'] = talib.MACD(data['Close'])

# Print out what kind of divergence, if any, was detected
if data['Close'][-1] > data['Close'][-2] and data['macd'][-1] < data['macd'][-2]:
    print('Bearish divergence detected!')
elif data['Close'][-1] < data['Close'][-2] and data['macd'][-1] > data['macd'][-2]:
    print('Bullish divergence detected!')
else:
    print('No divergence detected.')

