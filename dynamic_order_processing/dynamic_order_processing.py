
from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, order_amount: float) -> float:
        pass

class RegularDiscount(DiscountStrategy):
    def apply_discount(self, order_amount: float) -> float:
        return order_amount * 0.95  # 5% discount

class PremiumDiscount(DiscountStrategy):
    def apply_discount(self, order_amount: float) -> float:
        return order_amount * 0.90  # 10% discount

class VIPDiscount(DiscountStrategy):
    def apply_discount(self, order_amount: float) -> float:
        return order_amount * 0.85  # 15% discount

class Order:
    def __init__(self, customer_type: str, order_amount: float):
        self.customer_type = customer_type
        self.order_amount = order_amount

        if customer_type == "regular":
            self.discount_strategy = RegularDiscount()
        elif customer_type == "premium":
            self.discount_strategy = PremiumDiscount()
        elif customer_type == "VIP":
            self.discount_strategy = VIPDiscount()
        else:
            raise ValueError(f"Unknown customer type: {customer_type}")

    def final_price(self) -> float:
        return self.discount_strategy.apply_discount(self.order_amount)

if __name__ == "__main__":
    regular_order = Order("regular", 100.0)
    premium_order = Order("premium", 100.0)
    vip_order = Order("VIP", 100.0)

    print(f"Final price for regular customer: ${regular_order.final_price():.2f}")
    print(f"Final price for premium customer: ${premium_order.final_price():.2f}")
    print(f"Final price for VIP customer: ${vip_order.final_price():.2f}")
