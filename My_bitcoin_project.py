
import numpy as np
import numpy_financial as npf
import matplotlib.pyplot as plt
import yfinance as yf
#Task1: Calculate the Volatility of Bitcoin and output the Risk %
#Task2: Calculate tand output the Sharpe Ratio
#Need to calculate the returns

data = yf.Ticker('BTC-USD')


#Daily return
d = yf.download('BTC-USD', start='2020-01-01')

#Calculate percentage change
pc = d['Close'].pct_change()

x = data.history('1y')['Close']

start = 1000 / x[0]

#Volatility
#To do this use the std.dv of my returns 
vol = (np.std(d))

print(vol)


annual_std = np.std(vol) * np.sqrt(252)

print(annual_std)

y = np.multiply(start, x)
plt.plot(y)
plt.savefig('plot.png')