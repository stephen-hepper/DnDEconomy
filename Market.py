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
        #print(self.trade_goods)
        for good in self.trade_goods:
            # used as a quick check for now, need to expand to print all details
            if good is not None:
                print(f'{good.name:25s}{good.price_per_unit:10s}{good.unit_size:10s}{good.good_type:10s}'
                      f'{good.units_available:4}')
            else:
                print("Good is none")


'''
    if __name__ == '__main__':
        for file in os.listdir(path):
            print(file.split(".")[0])

'''
