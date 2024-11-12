import pytest
from products import Product

# Test 1: Creating a normal product
def test_create_normal_product():
    product = Product(name="Apple", price=1.0, quantity=10)
    assert product.name == "Apple"
    assert product.price == 1.0
    assert product.quantity == 10
    assert product.is_active() is True


# Test 2: Creating a product with invalid details (empty name, negative price)
def test_create_invalid_product():
    # Test empty name
    with pytest.raises(ValueError, match="name cannot be empty"):
        Product("", price=1450, quantity=100)

    # Test negative price
    with pytest.raises(ValueError, match="must be non-negative"):
        Product("MacBook Air M2", price=-10, quantity=100)

    # Test negative quantity
    with pytest.raises(ValueError, match="must be non-negative"):
        Product("MacBook Air M2", price=1450, quantity=-5)

# Test 3: Product becomes inactive when quantity reaches 0
def test_product_inactive_quantity_zero():
    product = Product(name="Laptop", price=1000, quantity=1)
    product.buy(1)  # Buying the only item in stock
    assert product.get_quantity() == 0
    assert product.is_active() is False
# Test 4: Product purchase modifies quantity and returns correct output
def test_product_purchase():
    product = Product(name="Laptop", price=1000, quantity=5)
    total_price = product.buy(3)
    assert total_price == 3000  # 3 * 1000
    assert product.get_quantity() == 2  # 5 - 3

# Test 5: Buying a larger quantity than exists invokes exception
def test_buying_more_than_available_quantity():
    product = Product(name="Tablet", price=300, quantity=2)
    with pytest.raises(Exception, match="Insufficient quantity in stock"):
        product.buy(5)
