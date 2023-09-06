#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install yfinance')


# In[2]:


import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


# In[4]:


# Create a Ticker object for Tesla (TSLA)
tsla = yf.Ticker("TSLA")

# Fetch historical data for the last year
tsla_data = tsla.history(period="1y")


# In[5]:


tsla_data.head()


# In[6]:


tsla_data.tail()


# In[14]:


# Create a Ticker object for GameStop (GME)
gme = yf.Ticker("GME")

# Fetch historical data for the last year
gme_data = gme.history(period="1y")


# In[8]:


gme_data.head()


# In[9]:


gme_data.tail()


# In[17]:


import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def make_graph(stock_symbol, start_date, end_date, title):
    # Create a Ticker object for the specified stock symbol
    stock = yf.Ticker(stock_symbol)
    
    # Fetch historical data for the specified date range
    stock_data = stock.history(start=start_date, end=end_date)
    
    # Plot the closing prices
    plt.figure(figsize=(12, 6))
    plt.plot(stock_data.index, stock_data['Close'], label=f'{stock_symbol} Close Price', color='blue')
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage of the make_graph function
make_graph("TSLA", "2022-01-01", "2023-01-01", "Tesla (TSLA) Stock Price (2022)")


# In[18]:


import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def make_graph(stock_symbol, title):
    # Create a Ticker object for the specified stock symbol
    stock = yf.Ticker(stock_symbol)
    
    # Fetch historical data for the last year
    stock_data = stock.history(period="1y")
    
    # Plot the closing prices
    plt.figure(figsize=(12, 6))
    plt.plot(stock_data.index, stock_data['Close'], label=f'{stock_symbol} Close Price', color='blue')
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Usage example for GameStop (GME) with a custom title
make_graph("GME", "GameStop (GME) Stock Price")


# In[ ]:




