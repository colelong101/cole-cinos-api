class IceStorm:
    _ice_storm_prices = {
        "Mint Chocolate Chip": 4.00,
        "Chocolate": 3.00,
        "Vanilla Bean": 3.00,
        "Banana": 3.50,
        "Butter Pecan": 3.50,
        "S'more": 4.00
    }

    _topping_prices = {
        "Cherry": 0.00,
        "Whipped Cream": 0.00,
        "Caramel Sauce": 0.50,
        "Chocolate Sauce": 0.50,
        "Storios": 1.00,
        "Dig Dogs": 1.00,
        "T&T's": 1.00,
        "Cookie Dough": 1.00,
        "Pecans": 0.50
    }

    def __init__(self, size):
        """Initialize the IceStorm class with a given size"""
        self._size = size
        self._flavors = []

    def get_flavors(self):
        """Get IceStorm flavors"""
        return self._flavors

    def add_flavor(self, flavor):
        """Add a flavor to the IceStorm"""
        if flavor not in self._flavors:
            self._flavors.append(flavor)
        else:
            raise ValueError("Invalid or duplicate flavor")

    def get_size(self):
        """Get IceStorm size"""
        return self._size

    def get_total(self):
        """Get IceStorm total price"""
        total = 0
        for flavor in self._flavors:
            total += self._ice_storm_prices[flavor]
        return total

    def get_num_flavors(self):
        """Get the number of flavors in the IceStorm drink."""
        return len(self._flavors)

    def __str__(self):
        """Return a formatted description of the IceStorm drink."""
        description = f"Size: {self._size}, Flavors: {', '.join(self._flavors)}"
        return description