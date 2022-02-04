import TradeGood
from pathlib import Path
import os


class Market(object):
    """
    A 'Market' is a physical place in the world (i.e. Gottstand). It has trade goods which make up the trade tables
    that we are used to in Roll-20
    """

    path = 'markets'

    def __init__(self, name="New_Market", trade_goods=None):
        self.name = name
        if trade_goods is None:
            trade_goods = []
        else:
            self.trade_goods = trade_goods

    def display_goods(self):
        for good in self.trade_goods:
            # used as a quick check for now, need to expand to print all details
            print(f'{good.name}')


'''
    if __name__ == '__main__':
        for file in os.listdir(path):
            print(file.split(".")[0])

'''
