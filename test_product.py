import pytest
from products import Product, NonStockedProduct, LimitedProduct
from promotions import SecondHalfPrice, ThirdOneFree, PercentDiscount
from store import Store

# Test 1: Creating a normal product
def test_create_normal_product():
    product = Product(name="Apple", price=1.0, quantity=10)
    assert product.name == "Apple"
    assert product.price == 1.0
    assert product.quantity == 10
    assert product.is_active() is True


# Test 2: Creating a product with invalid details
def test_create_invalid_product():
    # Test empty name
    with pytest.raises(ValueError, match="Product name cannot be empty"):
        Product("", price=1450, quantity=100)

    # Test negative price
    with pytest.raises(ValueError, match="Product price must be non-negative"):
        Product("MacBook Air M2", price=-10, quantity=100)

    # Test negative quantity
    with pytest.raises(ValueError, match="Product quantity must be non-negative"):
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
    with pytest.raises(ValueError, match="Not enough stock"):
        product.buy(5)


# Setup initial stock of inventory
def test_store_setup():
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
        NonStockedProduct("Windows License", price=125),
        LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
    ]

    # Create promotions
    second_half_price = SecondHalfPrice("Second Half price!")
    third_one_free = ThirdOneFree("Third One Free!")
    thirty_percent = PercentDiscount("30% off!", percent=30)

    # Add promotions to products
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)

    # Initialize store
    best_buy = Store(product_list)
    assert len(best_buy.get_all_products()) == 5
