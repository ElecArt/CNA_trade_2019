#!/usr/bin/python3

import sys
from update import *

def loop():
    while True:
        try:
            inputline = input()
        except(KeyboardInterrupt, EOFError):
            break
        inputline = inputline.split(" ")
        update(inputline)

if __name__ == "__main__":
    loop()