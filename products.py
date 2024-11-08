class Product:
    """Represents a product in a store with a name, price, and quantity."""

    def __init__(self, name: str, price: float, quantity: int):
        """
        Initializes a Product instance.

        Args:
            name (str): The name of the product.
            price (float): The price per unit of the product.
            quantity (int): The quantity of the product in stock.

        Raises:
            ValueError: If name is empty or if price/quantity are negative.
        """
        if not name or price < 0 or quantity < 0:
            raise ValueError(
                "Invalid input: name cannot be empty, and price/quantity must be non-negative."
            )

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> float:
        """Returns the current quantity of the product in stock."""
        return self.quantity

    def set_quantity(self, quantity: int):
        """
        Sets the quantity of the product. Deactivates the product if quantity is 0.

        Args:
            quantity (int): The new quantity to set.

        Raises:
            ValueError: If the quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """Returns True if the product is active, otherwise False."""
        return self.active

    def activate(self):
        """Activates the product, making it available for purchase."""
        self.active = True

    def deactivate(self):
        """Deactivates the product, making it unavailable for purchase."""
        self.active = False

    def show(self) -> str:
        """Returns a string representing the product details."""
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}"

    def buy(self, quantity: int) -> float:
        """
        Buys a given quantity of the product and returns the total price.

        Args:
            quantity (int): The quantity to purchase.

        Returns:
            float: The total price for the purchased quantity.

        Raises:
            ValueError: If quantity is non-positive.
            Exception: If the product is inactive or if requested quantity is unavailable.
        """
        if quantity <= 0:
            raise ValueError("Quantity to buy must be positive.")
        if not self.is_active():
            raise Exception("Product is inactive and cannot be purchased.")
        if quantity > self.quantity:
            raise Exception("Insufficient quantity in stock.")

        total_price = quantity * self.price
        self.set_quantity(self.quantity - quantity)
        return total_price

# Testing code (commented out to avoid unused variable warning)
# def main():
#     bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
#     # mac = Product("MacBook Air M2", price=1450, quantity=100)  # Unused variable
#     bose.set_quantity(1000)

# main()
