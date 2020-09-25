##
## EPITECH PROJECT, 2020
## CNA_trade_2019
## File description:
## trade_obj
##

class Param():
    settings = {}
    update = {}
    stack = {}
    candles = {}
    datas = {}
    i = 0
    j = 0
    a = 0
    b = 0
    c = 0
    curr = ['BTC_ETH', 'USDT_ETH', 'USDT_BTC']
    csv = ['high', 'low', 'open', 'close', 'volume']
    stock = {'USDT': {'total': 1000.0}, 'BTC': {'total' : 0, 'actions' : []}, 'ETH': {'total' : 0, 'actions' : []}}
    pair = {"BTC_ETH": {}, "USDT_ETH": {}, "USDT_BTC": {}}
    csv1 = {"date", "high", "low", "open", "close", "volume"}
    for i in pair:
        candles[i] = pair[i]
        for j in csv1:
            candles[i][j] = []
    ratios = {"average": {}, "rate": {}}
    types = {"BTC_ETH": {}, "USDT_ETH": {}, "USDT_BTC": {}}
    csv2 = {"high", "low", "open", "close", "volume"}
    for a in ratios:
        datas[a] = ratios[a]
        for b in types:
            datas[a][b] = types[b]
            for c in csv2:
                datas[a][b][c] = []