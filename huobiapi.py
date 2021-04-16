# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 21:08:25 2021

@author: FunnyGiraffe
"""

import requests
import pandas as pd
import socks
import socket

# 行展开显示
pd.set_option('expand_frame_repr',False)

# 配置代理
socks.set_default_proxy(socks.SOCKS5,'127.0.0.1',10808)
socket.socket = socks.socksocket

baseUrl = 'https://api.huobi.pro'
currencys = '/v1/common/currencys'
kline = '/market/history/kline?period=60min&size=200&symbol=btcusdt'


full_url_cur = baseUrl + currencys
full_url_kline = baseUrl + kline

# resp = requests.get(full_url_cur)

resp = requests.get(full_url_kline)

# print(resp)
# print(resp.status_code)
# print(resp.json())

r_json = resp.json()
data_list = r_json['data']

df = pd.DataFrame(data_list)
print(df)