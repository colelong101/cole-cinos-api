class Drink:
  """Class representing a drink."""

  possible_bases = ["water", "sbrite", "pokeacola", "mr_salt", "hill_fog", "leaf_wine"]
  possible_flavors = ["lemon", "cherry", "strawberry", "mint", "blueberry", "lime"]
  _drink_price = 1

  def __init__(self, base):
      """Initialize a drink with a specified base."""
      if base not in Drink.possible_bases:
          raise ValueError("Invalid or duplicate base")
      self._base = base
      self._flavors = []

  def get_base(self):
      """Get the base of the drink."""
      return self._base

  def get_flavors(self):
      """Get the flavors of the drink."""
      return self._flavors

  def get_total(self):
      """Get the total price of the drink."""
      return self._drink_price

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