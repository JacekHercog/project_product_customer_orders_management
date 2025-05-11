from collections import Counter
from dataclasses import dataclass
from decimal import Decimal
from src.model import Customer, Product, CustomerDataDict, ProductDataDict, OrderDataDict
from src.repository import PurchaseSummaryRepository, CustomersWithPurchesdProducts
import logging

logging.basicConfig(level=logging.INFO)

@dataclass(eq=False, frozen=False)
class PurchasesSummaryService:
    """
    Service class for analyzing purchase data.

    Attributes:
        repository (PurchaseSummaryRepository): A repository that provides summarized purchase data.

    Methods:
        calculate_avarage_spending_per_customer() -> dict[Customer, Decimal]:
            Calculate the average spending per customer.
        find_most_popular_products() -> list[Product]:
            Find the most popular products based on purchase quantities.
        find_highest_and_lowest_spenders() -> tuple[list[Customer], list[Customer]]:
            Identify the highest and lowest spenders among customers.
        calculate_total_spent(purchases: dict[Product, int]) -> Decimal:
            Calculate the total amount spent on purchases.
    """
    repository: PurchaseSummaryRepository[CustomerDataDict, ProductDataDict, OrderDataDict]

    def calculate_avarage_spending_per_customer(self) -> dict[Customer, Decimal]:
        """
        Calculate the average spending per customer.

        Returns:
            dict[Customer, Decimal]: A dictionary mapping each customer to their average spending.
        """
        average_spending: dict[Customer, Decimal] = {}
        for customer, purchases in self.repository.purchase_summary().items():
            total_spent = self.calculate_total_spent(purchases)
            total_products = Decimal(sum(purchases.values()))
            average_spending[customer] = total_spent / total_products if total_products > 0 else Decimal("0.0")
        return average_spending

    def find_most_popular_products(self) -> list[Product]:
        """
        Find the most popular products based on purchase quantities.

        Returns:
            list[Product]: A list of the most popular products. If there are multiple products with the same
            highest quantity, all are included.
        """
        product_counter: Counter[Product] = Counter()

        for purchases in self.repository.purchase_summary().values():
            for product, quantity in purchases.items():
                product_counter[product] += quantity

        if not product_counter:
            return []
        max_count = max(product_counter.values())

        return [product for product, count in product_counter.items() if count == max_count]

    def find_highest_and_lowest_spenders(self) -> tuple[list[Customer], list[Customer]]:
        """
        Identify the highest and lowest spenders among customers.

        Returns:
            tuple[list[Customer], list[Customer]]:
                - A list of customers who spent the most.
                - A list of customers who spent the least.
        """
        max_spent = Decimal("-Infinity")
        min_spent = Decimal("Infinity")
        highest_spenders: list[Customer] = []
        lowest_spenders: list[Customer] = []

        for customer, purchases in self.repository.purchase_summary().items():
            total_spent = self.calculate_total_spent(purchases)
            if total_spent > max_spent:
                max_spent = total_spent
                highest_spenders = [customer]
            elif total_spent == max_spent:
                highest_spenders.append(customer)

            if total_spent < min_spent:
                min_spent = Decimal(total_spent)
                lowest_spenders = [customer]
            elif total_spent == min_spent:
                lowest_spenders.append(customer)

        return highest_spenders, lowest_spenders

    @staticmethod
    def calculate_total_spent(purchases: dict[Product, int]) -> Decimal:
        """
        Calculate the total amount spent on purchases.

        Args:
            purchases (dict[Product, int]): A dictionary mapping products to their purchased quantities.

        Returns:
            Decimal: The total amount spent on the purchases.
        """
        return sum((product.total_price(quantity) for product, quantity in purchases.items()), Decimal("0.0"))

