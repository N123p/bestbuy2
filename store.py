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

        Args:
            shopping_list (List[Tuple[Product, int]]): A list of tuples, each containing
            a Product instance and the quantity to purchase.

        Returns:
            float: The total price of the entire order.
        """
        total_price = 0.0

        for product, quantity in shopping_list:
            # Ensure the product is in the store's inventory and active
            if product not in self.products or not product.is_active():
                raise ValueError(f"Product '{product.name}' is not available or inactive in the store.")

            # Calculate price with promotion if applicable
            if product.promotion:
                total_price += product.promotion.apply_promotion(product, quantity)
            else:
                total_price += product.buy(quantity)

        return total_price
