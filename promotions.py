from abc import ABC, abstractmethod

class Promotion(ABC):
    """Abstract base class for promotions."""

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:
        """Calculates and returns the total price after applying the promotion."""
        pass


class PercentDiscount(Promotion):
    """Applies a percentage discount."""

    def __init__(self, name: str, percent: float):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity) -> float:
        discount_price = product.price * (1 - self.percent / 100)
        return discount_price * quantity


class SecondHalfPrice(Promotion):
    """Applies a promotion where the second item is half price."""

    def apply_promotion(self, product, quantity) -> float:
        full_price_count = quantity // 2 + quantity % 2
        half_price_count = quantity // 2
        return (full_price_count * product.price) + (half_price_count * product.price * 0.5)


class ThirdOneFree(Promotion):
    """Applies a promotion where every third item is free."""

    def apply_promotion(self, product, quantity) -> float:
        paid_items = (quantity // 3) * 2 + (quantity % 3)
        return paid_items * product.price
