class Order:
  """Class representing an order."""

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