class RetailItem:
    # set attributes
    def __init__(self, item, units, price):
        self.__item_description = item
        self.__item_units = units
        self.__item_price = price

    # set methods
    def set_desc(self, item):
        self.__item_description = item

    def set_units(self, units):
        self.__item_units = units

    def set_price(self, price):
        self.__item_price = price

    # return values
    def get_desc(self):
        return self.__item_description

    def get_units(self):
        return self.__item_units

    def get_price(self):
        return self.__item_price

    """
    item1 = ["Jacket", "12", 59.95]
    item2 = ("Designer Jeans", 40, 34.95)
    item3 = ("Shirt", 20, 24.95)
    """
