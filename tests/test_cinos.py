from api.Drink import Drink
from api.Order import Order

def test_get_base():
    """Test the getter for the base of the drink."""
    drink = Drink("sbrite")
    assert drink.get_base() == "sbrite"

def test_get_flavors_empty():
    """Test case to check if get_flavors returns an empty list when flavors are not set."""
    drink = Drink("water")
    assert drink.get_flavors() == []

def test_get_total():
    """Test if get_total method returns the correct drink price."""
    drink = Drink("water")
    assert drink.get_total() == 1

def test_get_num_flavors_if_empty():
    """Test if get_num_flavors returns 0 when no flavors are set."""
    drink = Drink("water")
    assert drink.get_num_flavors() == 0

def test_get_num_flavors_if_not_empty():
    """Test if get_num_flavors returns the correct number of flavors when flavors are set."""
    drink = Drink("water")
    flavors = ["lemon", "mint", "blueberry"]
    drink.set_flavors(flavors)
    assert drink.get_num_flavors() == len(flavors)

def test_set_flavors():
    """Test if set_flavors method correctly sets the flavors."""
    drink = Drink("water")
    flavors = ["lemon", "mint", "blueberry"]
    drink.set_flavors(flavors)
    assert drink.get_flavors() == flavors

def test_add_flavor():
    """Test adding a valid flavor using the add_flavor method."""
    drink = Drink("water")
    drink.add_flavor("lemon")
    assert drink.get_flavors() == ["lemon"]

def test_duplicate_add_flavor():
    """Test adding a duplicate flavor and check if the correct exception is raised."""
    drink = Drink("water")
    drink.add_flavor("lemon")
    try:
        drink.add_flavor("lemon")
    except ValueError as ve:
        assert str(ve) == "Invalid or duplicate flavor"

def test_get_items_when_empty():
    """Test if get_items returns an empty array when no items are added to the order."""
    order = Order()
    assert order.get_items() == []

def test_get_num_items_when_empty():
    """Test if get_num_items returns 0 when no items are added to the order."""
    order = Order()
    assert order.get_num_items() == 0

def test_get_total_when_empty():
    """Test if get_total returns 0 when no items are added to the order."""
    order = Order()
    assert order.get_total() == 0

def test_add_item():
    """Test if add_item correctly adds a drink to the order."""
    order = Order()
    drink = Drink("water")
    order.add_item(drink)
    assert order.get_items() == [drink]

def test_remove_item_valid_index():
    """Test if remove_item removes the item at a valid index."""
    order = Order()
    drink1 = Drink("water")
    drink2 = Drink("sbrite")
    order.add_item(drink1)
    order.add_item(drink2)
    order.remove_item(0)
    assert order.get_items() == [drink2]

def test_remove_item_invalid_index():
    """Test if remove_item does nothing for an invalid index."""
    order = Order()
    drink = Drink("water")
    order.add_item(drink)
    order.remove_item(1)
    assert order.get_items() == [drink]

def test_size_and_cost():
    drink = Drink("sbrite", "medium")
    assert drink.get_size() == "medium"
    assert drink.get_total() == 1.75

def test_set_size_case_insensitive():
    drink = Drink("sbrite", "small")
    drink.set_size("MEGa")
    assert drink.get_size() == "mega"
    assert drink.get_total() == 2.15

def test_get_total_with_flavors_and_size():
    drink = Drink("sbrite", "large")
    drink.add_flavor("lemon")
    assert drink.get_total() == 2.05 + 0.15

def test_get_size_accessor():
    drink = Drink("sbrite", "medium")
    assert drink.get_size() == "medium"

def test_set_size_accessor():
    drink = Drink("sbrite", "medium")
    drink.set_size("large")
    assert drink.get_size() == "large"

def test_generate_receipt_with_sizes_and_flavors():
    order = Order()
    drink1 = Drink("sbrite", "medium")
    drink1.add_flavor("lemon")
    drink2 = Drink("water", "small")
    order.add_item(drink1)
    order.add_item(drink2)

    receipt = order.generate_receipt()
    assert receipt["num_beverages"] == 2
    assert receipt["beverage_details"][0]["base"] == "sbrite"
    assert receipt["beverage_details"][0]["size"] == "medium"
    assert receipt["beverage_details"][0]["total"] == drink1.get_total()
    assert receipt["beverage_details"][1]["base"] == "water"
    assert receipt["beverage_details"][1]["size"] == "small"
    assert receipt["beverage_details"][1]["total"] == drink2.get_total()
    assert receipt["total_cost"] == drink1.get_total() + drink2.get_total()
    assert receipt["tax"] == 0.0725 * (drink1.get_total() + drink2.get_total())
    assert receipt["overall_total"] == 1.0725 * (drink1.get_total() + drink2.get_total())
