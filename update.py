##
## EPITECH PROJECT, 2020
## CNA_trade_2019
## File description:
## update
##

from trade_obj import *
from compute import *
from actions import *

def parse_input(param, update, game, flag, inputline):
    if update == "settings":
        param.settings[game] = flag
    elif update == "update":
        if flag == "next_candles":
            pair = inputline[3]
            pair = pair.split(";")
            for line in pair:
                line = line.split(",")
                curr = line[0]
                line.pop(0)
                for i, j in zip(param.csv, range(6)):
                    param.candles[curr][i].append(line[j])
            compute()
            param.update[flag] = param.candles
        elif flag == "stacks":
            pair = inputline[3]
            pair = pair.split(',')
            for line in pair:
                line = line.split(":")
                curr = line[0]
                line.pop(0)
                param.stack[curr] = line[0]
    elif update == "action" and game == "order":
        data = int(flag)
        actions(data)

def update(inputline):
    param = Param()
    update = inputline[0]
    game = inputline[1]
    next_candles = inputline[2]
    parse_input(param, update, game, next_candles, inputline)

