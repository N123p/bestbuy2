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
        """
        Calculates and returns the total quantity of all products in the store,
        excluding NonStockedProduct which has unlimited stock.
        """
        return sum(
            product.get_quantity()
            for product in self.products
            if not isinstance(product, NonStockedProduct)
        )

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

        Raises:
            ValueError: If any requested quantity is more than the available stock of that product,
            or if a product in the order is inactive or not available in the store's inventory.
        """
        total_price = 0.0

        for product, quantity in shopping_list:

            if product not in self.products:
                raise ValueError(f"Product '{product.name}' is not available in the store.")
            if not product.is_active():
                raise ValueError(f"Product '{product.name}' is inactive and cannot be purchased.")
            if isinstance(product, NonStockedProduct):
                total_price += product.buy(quantity)
            elif isinstance(product, LimitedProduct):
                if quantity > product.maximum:
                    raise ValueError(
                        f"Cannot buy more than {product.maximum} of '{product.name}' in a single order."
                    )
                total_price += product.buy(quantity)
            else:
                if quantity > product.get_quantity():
                    raise ValueError(
                        f"Not enough quantity for '{product.name}'. "
                        f"Requested: {quantity}, Available: {product.get_quantity()}"
                    )
                    total_price += product.buy(quantity)

        return total_price
