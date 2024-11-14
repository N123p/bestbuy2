from typing import List, Tuple
from products import Product, NonStockedProduct, LimitedProduct

class Store:
    """A Store that manages a list of products with various operations."""

    def __init__(self, products: List[Product]):
        """Initialize the Store with a list of Product instances."""
        self.products = products

    def add_product(self, product: Product):
        """Adds a product to the store's product list."""
        self.products.append(product)

    def remove_product(self, product: Product):
        """Removes a product from the store's product list if it exists."""
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Calculates and returns the total quantity of all products in the store."""
        return sum(product.get_quantity() for product in self.products if not isinstance(product, NonStockedProduct))

    def get_all_products(self) -> List[Product]:
        """Returns a list of all active products in the store."""
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        """
        Places an order for multiple products and returns the total cost.
        """
        total_price = 0.0

        for product, quantity in shopping_list:
            # Check that the product is in the store and is active
            if product not in self.products or not product.is_active():
                raise ValueError(f"Product '{product.name}' is not available or inactive in the store.")

            # Apply promotion if available
            if product.promotion:
                total_price += product.promotion.apply_promotion(product, quantity)
                # Reduce the quantity after promotion is applied
                product.buy(quantity)  # This reduces the stock count after promotional purchase
            else:
                total_price += product.buy(quantity)  # This will handle stock reduction for regular purchases

        return total_price
