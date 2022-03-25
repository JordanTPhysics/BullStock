# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 23:45:28 2022

@author: starg
"""

import requests

RAPID_API_HOST = "finage-currency-data-feed.p.rapidapi.com"

RAPID_API_KEY = "3d2d033525msh24e9407d64492a6p13ac35jsna63236540ffe"



url = "https://finage-currency-data-feed.p.rapidapi.com/history"

querystring = {"currency":"EURUSD","from":"2015-01-05","to":"2015-01-07","apikey":"API_KEYUX0RG2F4BXCV5JJ50P0K3BLFQOS0Q0DP"}

headers = {
    'x-rapidapi-host': "finage-currency-data-feed.p.rapidapi.com",
    'x-rapidapi-key': "3d2d033525msh24e9407d64492a6p13ac35jsna63236540ffe"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text,response.status_code)