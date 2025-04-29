#!/usr/bin/env python
# coding: utf-8

# In[81]:


get_ipython().system('pip install yfinance')
#!pip install pandas
#!pip install requests
get_ipython().system('pip install bs4')
#!pip install plotly
get_ipython().system(' pip install html5lib')
get_ipython().system(' pip install requests')


# In[84]:


import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# In[85]:


tesla=yf.Ticker('TSLA')


# In[86]:


tesla_data=tesla.history(period="max")


# In[87]:


tesla_data.reset_index(inplace=True)
tesla_data.head()


# In[75]:





# In[112]:


url=" https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36"
}
html_data = requests.get(url, headers=headers).text


# In[113]:


soup = BeautifulSoup(html_data, "html.parser")


# In[116]:


table = soup.find("table", {"class": "historical_data_table table"})

data = []

if table is not None:
    tbody = table.find("tbody")
    
    for row in tbody.find_all("tr"):
        cols = row.find_all("td")
        if len(cols) == 2:
            date = cols[0].text.strip()
            revenue = cols[1].text.strip().replace("$", "").replace(",", "")
            data.append({"Date": date, "Revenue": revenue})  # <-- collect

    tesla_revenue = pd.DataFrame(data)

    tesla_revenue.dropna(inplace=True)
    tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]
    print(tesla_revenue.tail())

else:
    print("Table not found!")


# In[120]:


gme=yf.Ticker('GME')


# In[121]:


gme_data=tesla.history(period="max")


# In[122]:


gme_data.reset_index(inplace=True)
gme_data.head()


# In[130]:


url=" https://www.macrotrends.net/stocks/charts/GME/gamestop/revenuee"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36"
}
html_data = requests.get(url, headers=headers).text


# In[131]:


soup = BeautifulSoup(html_data, "html.parser")


# In[132]:


table = soup.find("table", {"class": "historical_data_table table"})

data = []

if table is not None:
    tbody = table.find("tbody")
    
    for row in tbody.find_all("tr"):
        cols = row.find_all("td")
        if len(cols) == 2:
            date = cols[0].text.strip()
            revenue = cols[1].text.strip().replace("$", "").replace(",", "")
            data.append({"Date": date, "Revenue": revenue})  # <-- collect

    gme_revenue = pd.DataFrame(data)

    gme_revenue.dropna(inplace=True)
    gme_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]
    print( gme_revenue.tail())

else:
    print("Table not found!")


# In[140]:


make_graph(tesla_data, tesla_revenue, 'Tesla')


# In[141]:


make_graph(gme_data, gme_revenue, 'GameStop')


# In[ ]:




