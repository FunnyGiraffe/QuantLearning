# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 01:09:42 2021

@author: FunnyGiraffe
"""

import requests
import socks
import socket
import time

# 配置代理
socks.set_default_proxy(socks.SOCKS5,'127.0.0.1',10808)
socket.socket = socks.socksocket

baseUrl = 'https://api.binance.com'

kline = '/api/v3/klines'
depth = '/api/v3/depth'

limit = 1000
endTime = int(time.time() * 1000)
startTime = int(endTime - limit * 60 * 1000)
# print(int(time.time() * 1000))
klineFullUrl = baseUrl + kline + '?' + 'symbol=BTCUSDT&interval=1m&limit=' + str(limit) + '&startTime=' + str(startTime) + '&endTime=' + str(endTime)
print(klineFullUrl)

resp = requests.get(klineFullUrl)
print(resp.json())