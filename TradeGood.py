import random
from pathlib import Path

class TradeGood():

    #CSV FILE:
    #NAME, PRICE_PER_UNIT, UNIT_SIZE, GOOD_TYPE (TRADE, WEAPON, ARMOR), UNITS_AVAILABLE

    def __init__(self, name = "N/A", price_per_unit = 1, unit_size = 10, good_type = None, units_available = 0  ):
        self.name = name
        self.price_per_unit = price_per_unit
        self.unit_size = unit_size
        self.good_type = good_type
        self.units_available = units_available




