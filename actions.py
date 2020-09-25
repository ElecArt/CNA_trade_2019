##
## EPITECH PROJECT, 2020
## CNA_trade_2019
## File description:
## actions
##

from trade_obj import *

def eth_action(param):
    i = 0
    sell = 0

    while (i < len(param.stock['ETH']['actions'])):
        if (float(param.update['next_candles']['USDT_ETH']['high'][-1]) > 1):
            if (float(param.update['next_candles']['USDT_ETH']['close'][-1]) > param.stock['ETH']['actions'][i]['price'] + 500):
                sell += param.stock['ETH']['actions'][i]['amount']
                param.stock['ETH']['total'] -= param.stock['ETH']['actions'][i]['amount']
                del param.stock['ETH']['actions'][i]
        i += 1
    if (sell != 0):
        print("sell USDT_ETH " + str(sell))
        param.stock['USDT']['total'] += sell * float(param.update['next_candles']['USDT_ETH']['close'][-1]) * 0.998
        return

def usdt_action(param):
    s_usdt = param.stock['USDT']['total'] / 2
    close = float(param.update['next_candles']['USDT_ETH']['close'][-1])
    amount = s_usdt / close
    print("buy USDT_ETH " + str(amount))
    param.stock['ETH']['actions'].append({'price': close,'amount': amount * 0.998})
    param.stock['ETH']['total'] += amount * 0.998
    param.stock['USDT']['total'] -= s_usdt

def actions(time):
    param = Param()

    if (param.stock['ETH']['total'] != 0):
        eth_action(param)
    else:
        while True:
            usdt_action(param)
            return
    print ("pass")