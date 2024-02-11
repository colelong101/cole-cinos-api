class Order:
    """Class representing an order."""
    TAX_RATE = 0.0725

    def __init__(self):
        """Initialize an order with an empty list of items."""
        self._items = []

    def get_items(self):
        """Get the items in the order."""
        return self._items

    def get_num_items(self):
        """Get the number of items in the order."""
        return len(self._items)

    def get_total(self):
        """Get the total price of the order."""
        total = 0
        for item in self._items:
            total += item.get_total()
        return total

    def add_item(self, drink):
        """Add a drink to the order."""
        self._items.append(drink)

    def remove_item(self, index):
        """Remove a drink from the order based on index."""
        if 0 <= index < len(self._items):
            del self._items[index]

    def generate_receipt(self):
        """Generate a receipt for the order."""
        receipt = {
            "num_beverages": self.get_num_items(),
            "beverage_details": [],
            "total_cost": self.get_total(),
            "tax": self.TAX_RATE * self.get_total(),
            "overall_total": (1 + self.TAX_RATE) * self.get_total()
        }
        for item in self._items:
            beverage_detail = {
                "base": item.get_base(),
                "size": item.get_size(),
                "total": item.get_total()
            }
            receipt["beverage_details"].append(beverage_detail)
        return receipt
