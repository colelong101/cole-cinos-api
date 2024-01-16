""" defining the possible bases and flavors provided by cinos """
possible_bases = ["water", "sbrite", "pokeacola", "mr_salt", "hill_fog", "leaf_wine"]
possible_flavors = ["lemon", "cherry", "strawberry", "mint", "blueberry", "lime"];


class Drink:
    def __init__(self, base):
        """ simple validation to check valid base input """
        if base not in possible_bases:
            raise ValueError("Invalid or duplicate base")
        """ sets private attribute of 'base' """
        self.__base = base
        self.__flavors = []

    """ get_base method initializes and returns the value of 'base' """
    def get_base(self):
        return self.__base
    
    def get_flavors(self):
        return self.__flavors
    
    """This method gets the total number flavors, and adds 1 to represent the $1 charge per drink, and the $1 additional cost per flavor"""
    def get_total(self):
        return 1 + len(self.__flavors)
    
    def get_num_flavors(self):
        return len(self.__flavors)
    
    def set_flavors(self, flavors):
        self.__flavors = flavors
    
    def add_flavor(self, flavor):
        """ simple validation to check valid flavor input """
        if flavor not in self.__flavors:
          self.__flavors.append(flavor)
        else:
          raise ValueError("Invalid or duplicate flavor")


class Order:
    def __init__(self):
      self.__items = []

    def get_items(self):
        return self.__items
    
    def get_num_items(self):
        return len(self.__items)
    
    def get_total(self):
        total = 0
        for item in self.__items:
            total += item.get_total()
        return total
    
    def add_item(self, drink):
        self.__items.append(drink)

    def remove_item(self, index):
        if 0 <= index < len(self.__items):
            del self.__items[index]



# testDrink = Drink("")
# print(testDrink.__base)

# yumDrink = Drink("water")
# yumDrink.add_flavor("lemon")

# order = Order()
# order.add_item(yumDrink)
            
# print("You have", order.get_num_items(), "drink(s) in your order")
# print("Your total for the order is:", "$", order.get_total())