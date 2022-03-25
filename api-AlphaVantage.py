# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 08:35:25 2022

@author: starg
"""



import requests
import pandas as pd
import matplotlib.pyplot as plt
import os
from scipy.optimize import curve_fit




API_KEY = os.environ['ALPHA_V_KEY']
chart_range = 'TIME_SERIES_INTRADAY'
asset = 'AAPL'
time = '5min'



def build_url(chart_range, asset, time):
    
    BASE_URL = f'https://www.alphavantage.co/query?function={chart_range}&symbol={asset}&interval={time}&apikey=48K05F2EQTGK1R9Y'

    
    return BASE_URL

def get_data(url):
    
    res = requests.get(url)
    data = res.json()
    
    return data


BASE_URL = build_url(chart_range, asset, time)
data = get_data(BASE_URL)

def format_data(dict_data):
    
    extracted = dict_data[f'Time Series ({time})']
    data = pd.DataFrame.from_dict(extracted).T
    index = [i for i in range(len(data))]
    data.set_index(index)
    return data

df = format_data(data)

times = df['Index']

def calc_average(data):
    opens = data['1. open']
    closes = data['4. close']
    highs = data['2. high']
    lows = data['3. low']
    
    avgs = []
    for i in range(len(data)):
        avg = (opens[i] + closes[i] + highs[i] + lows[i])/4
        avgs.append(avg)
        
    return avgs

plt.plot(times, calc_average(df), 'm-')
plt.show()

def plot_chart(times, prices):
    op = prices[0]
    high = prices[1]
    low = prices[2]
    close = prices[3]
    volume = prices[4]
    plot = plt.plot(times, high, 'r-')
    plot = plt.plot(times, op, 'b-')
    plot = plt.plot(times, low, 'g-')
    plot = plt.plot(times, close, 'm-')
   
    plt.show()
    return plot



