# Defining the possible bases and flavors provided by Cinos
possible_bases = ["water", "sbrite", "pokeacola", "mr_salt", "hill_fog", "leaf_wine"]
possible_flavors = ["lemon", "cherry", "strawberry", "mint", "blueberry", "lime"]


class Drink:
    _drink_price = 1

    def __init__(self, base):
        """Simple validation to check valid base input."""
        if base not in possible_bases:
            raise ValueError("Invalid or duplicate base")
        """Sets private attribute of 'base'."""
        self._base = base
        self._flavors = []

    def get_base(self):
        """Get_base method initializes and returns the value of 'base'."""

    def get_flavors(self):
        return self._flavors

    def get_total(self):
        """Get_total returns the value of the drink_price class var."""
        return self._drink_price

    def get_num_flavors(self):
        """Get_num_flavors returns the length of the flavors array."""
        return len(self._flavors)

    def set_flavors(self, flavors):
        """Set_flavors is the setter function to initialize the flavors based on input."""
        self._flavors = flavors

    def add_flavor(self, flavor):
        """Simple validation to check valid flavor input."""
        if flavor not in self._flavors:
            self._flavors.append(flavor)
        else:
            raise ValueError("Invalid or duplicate flavor")


class Order:
    def __init__(self):
        self._items = []

    def get_items(self):
        """Get_items retrieves values of items array."""
        return self._items

    def get_num_items(self):
        """Get_num_items returns the length of the flavors array."""
        return len(self._items)

    def get_total(self):
        """Total is initialized at zero."""
        total = 0
        for item in self._items:
            """Iterating over each drink in the order."""
            total += item.get_total()
            """Adding result of get_total for each item to the total var."""
        return total

    def add_item(self, drink):
        """Adds the provided drink to ._items array."""
        self._items.append(drink)

    def remove_item(self, index):
        """Checks index less than the length of ._items."""
        if 0 <= index < len(self._items):
            """Removes the item at index."""
            del self._items[index]
