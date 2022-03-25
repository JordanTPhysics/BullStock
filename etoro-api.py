# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 23:21:36 2022

@author: starg
"""




########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '{subscription key}',
}

params = urllib.parse.urlencode({
})

try:
    conn = http.client.HTTPSConnection('https://etoro-cdn.etorostatic.com')
    conn.request("GET", "https://etoro-cdn.etorostatic.com/web-client/et/fonts/dinot/DINOT.otf" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}")

####################################

