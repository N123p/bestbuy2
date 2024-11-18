class Product:
    """
    Represents a product in a store with a name, price, and quantity.

    This class includes methods to manage stock, apply promotions, and display product information.
    """
    def __init__(self, name: str, price: float, quantity: int = 0):
        """Initialize a Product with a name, price, and initial quantity."""
        if not name.strip():
            raise ValueError("Product name cannot be empty")
        if price < 0:
            raise ValueError("Product price must be non-negative")
        if quantity < 0:
            raise ValueError("Product quantity must be non-negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.promotion = None  # Promotion starts as None

    def set_promotion(self, promotion):
        """Sets a promotion for the product."""
        self.promotion = promotion

    def get_quantity(self) -> int:
        """Returns the current quantity of the product."""
        return self.quantity

    def is_active(self) -> bool:
        """Checks if the product is active (has quantity > 0)."""
        return self.quantity > 0

    def buy(self, quantity: int) -> float:
        """Reduces the product quantity and returns the cost for the given quantity."""
        if quantity > self.quantity:
            raise ValueError("Not enough stock")
        self.quantity -= quantity
        return self.price * quantity

    def show(self) -> str:
        """Displays product information, including promotion if set."""
        promotion_text = f"Promotion: {self.promotion.name}!" if self.promotion else "Promotion: None"
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}, {promotion_text}"


class NonStockedProduct(Product):
    def __init__(self, name: str, price: float):
        """Initialize a NonStockedProduct with unlimited quantity."""
        super().__init__(name, price)
        self.quantity = float('inf')  # Represent unlimited stock as infinity

    def get_quantity(self) -> str:
        """Overrides quantity display for unlimited products."""
        return "Unlimited"

    def buy(self, quantity: int) -> float:
        """Overrides buy to allow unlimited purchase without reducing stock."""
        return self.price * quantity

    def show(self) -> str:
        """Displays information specific to NonStockedProduct."""
        promotion_text = f"Promotion: {self.promotion.name}!" if self.promotion else "Promotion: None"
        return f"{self.name}, Price: ${self.price}, Quantity: Unlimited, {promotion_text}"


class LimitedProduct(Product):
    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        """Initialize a LimitedProduct with a maximum purchase limit per order."""
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity: int) -> float:
        """Ensures the purchase quantity does not exceed the maximum allowed."""
        if quantity > self.maximum:
            raise ValueError(f"Only {self.maximum} of this product can be purchased at a time.")
        # Call the parent `buy()` method to handle stock reduction and pricing
        return super().buy(quantity)

    def show(self) -> str:
        """Displays information specific to LimitedProduct."""
        promotion_text = f"Promotion: {self.promotion.name}!" if self.promotion else "Promotion: None"
        return f"{self.name}, Price: ${self.price}, Limited to {self.maximum} per order!, {promotion_text}"
