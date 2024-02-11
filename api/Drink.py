class Drink:
    """Class representing a drink."""

    possible_bases = ["water", "sbrite", "pokeacola", "mr_salt", "hill_fog", "leaf_wine"]
    possible_flavors = ["lemon", "cherry", "strawberry", "mint", "blueberry", "lime"]
    _drink_price = {
        "small": 1.50,
        "medium": 1.75,
        "large": 2.05,
        "mega": 2.15
    }
    _flavor_price = 0.15

    def __init__(self, base, size):
        """Initialize a drink with a specified base and size."""
        if base not in Drink.possible_bases:
            raise ValueError("Invalid or duplicate base")
        self._base = base
        self._size = size
        self._flavors = []

    def get_base(self):
        """Get the base of the drink."""
        return self._base

    def get_size(self):
        """Get the size of the drink."""
        return self._size

    def set_size(self, size):
        """Set the size of the drink."""
        size = size.lower()
        if size not in Drink._drink_price:
            raise ValueError("Invalid size")
        self._size = size

    def get_flavors(self):
        """Get the flavors of the drink."""
        return self._flavors

    def get_total(self):
        """Get the total price of the drink."""
        total = Drink._drink_price[self._size]
        total += len(self._flavors) * Drink._flavor_price
        return total

    def get_num_flavors(self):
        """Get the number of flavors in the drink."""
        return len(self._flavors)

    def set_flavors(self, flavors):
        """Set the flavors of the drink."""
        self._flavors = flavors

    def add_flavor(self, flavor):
        """Add a flavor to the drink."""
        if flavor not in self._flavors:
            self._flavors.append(flavor)
        else:
            raise ValueError("Invalid or duplicate flavor")
        
    def __str__(self):
        """Return a formatted description of the beverage."""
        description = f"Base: {self._base}, Size: {self._size}"
        if self._flavors:
            description += f", Flavors: {', '.join(self._flavors)}"
        return description

    @property
    def cost(self):
        """Live calculation of the total cost of the drink."""
        total = self._drink_price[self._size]
        total += len(self._flavors) * self._flavor_price
        return total


drink = Drink("hill_fog", "medium")
drink.add_flavor("lemon")

print("Description of Drink:")
print(drink)

print("\nLive Calculation of Total Cost:")
print(f"Total Cost: ${drink.cost:.2f}")