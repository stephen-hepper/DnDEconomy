from Market import Market
from TradeGood import TradeGood
import os


class Hub(object):
    """
    A Hub is a term for a collection of markets, not a physical location (unless we want it to be). Initial idea is to
    have it contain ALL markets, but it could be used to more realistically contain a subset of
    markets (by region, by kingdom, etc.).
    """

    path = "markets"

    def __init__(self, market_list=None, name="placeholder"):
        if market_list is None:
            market_list = []

        self.market_list = market_list
        self.name = name
        self.populate_markets()

    def populate_markets(self):
        #goods = []

        for file in os.listdir(Hub.path):

            m_name = file.split(".")[0]
            goods = []
            print(f'market name: {m_name}')
            with open(os.path.join(Hub.path, file)) as f:
                header = f.readline()
                for line in f.readlines():
                    item = (line.strip('\n').split(","))
                    if(len(item) != 5):
                        print(f'item-length: {len(item)}')  #test
                    print(f'item-description: {item}')      #test
                    #print(item[0], item[1], item[2], item[3], item[4])
                    tg = TradeGood(item[0], item[1], item[2], item[3], item[4])
                    goods.append(tg)

            m = Market(m_name, goods)
            self.market_list.append(m)

    def display_markets(self):
        for market in self.market_list:
            print(f'\nMarket: {market.name.upper()}')
            print(f'NAME\t\tPRICE\t\tUNIT_SIZE\t\tGOOD_TYPE\t\tUNITS_AVAILABLE')
            print(f'-----------------------------------------------------------')
           # print("%5s %10s %10s %10s" % ("NAME","PRICE","UNIT_SIZE","UNIT_AVAILABLE"))
            #print(f'NAME\t\t\tPRICE\t\t\tUNIT_SIZE\t\t\tGOOD_TYPE\t\t\tUNITS_AVAILABLE')
            print(market.display_goods())

if __name__ == '__main__':
    h = Hub()
    h.display_markets()
