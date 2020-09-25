##
## EPITECH PROJECT, 2020
## CNA_trade_2019
## File description:
## compute
##

from trade_obj import *

def compute():
    param = Param()

    for i in param.curr:
        for j in param.csv:
            if (len(param.candles[i][j]) >= 20):
                average = 0
                for k in param.candles[i][j][-20:]:
                    average += float(k)
                param.datas['average'][i][j].append(average / 20)
                rate = (float(param.candles[i][j][-1]) - float(param.candles[i][j][-20])) / float(param.candles[i][j][-20])
                param.datas['rate'][i][j].append(rate * 100)