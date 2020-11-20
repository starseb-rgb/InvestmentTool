# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


-----

# INVESTMENT TOOL

# 0) Strategy
# DUAL MOVING AVERAGE CROSSOVER
#   ... BUY when short-term average crosses long-term average and rises ABOVE it
#   ... SELL when short-term average crosses long-term average and rises BELOW it

# 1) Import libraries
from PyQt5.QtWidgets import *                   # for visuals
from pycoingecko import CoinGeckoAPI as cg      # Coinggecko API
import numpy as np                              # most financial analysis are done in 2D
import pandas as pd                             # for data analytics
import matplotlib as matpl                      # embedding plots

