from decimal import Decimal
from unittest.mock import MagicMock
from src.repository import PurchaseSummaryRepository, CustomersWithPurchesdProducts
from src.service import PurchasesSummaryService
from src.model import Customer, Product
import pytest

import logging
logging.basicConfig(level=logging.DEBUG)

def test_calculate_average_with_no_purchases(
        service: PurchasesSummaryService,
        customer_1: Customer,
        mock_repository: MagicMock) -> None:
    """
    Test the calculation of average spending when there are no purchases.

    Args:
        service (PurchasesSummaryService): The service instance to test.
        customer_1 (Customer): A sample customer instance.
        mock_repository (MagicMock): A mock repository for purchase summary data.

    Asserts:
        - The average spending for the customer is 0.0 when there are no purchases.
    """
    # Test with no purchases
    mock_repository.purchase_summary.return_value = {customer_1: {}}
    result = service.calculate_avarage_spending_per_customer()
    assert result[customer_1] == Decimal("0.0")

def test_calculate_avarage_with_one_product(
        service: PurchasesSummaryService,
        customer_1: Customer,
        product_1: Product,
        mock_repository: MagicMock) -> None:
    """
    Test the calculation of average spending when the customer has purchased one product.

    Args:
        service (PurchasesSummaryService): The service instance to test.
        customer_1 (Customer): A sample customer instance.
        product_1 (Product): A sample product instance.
        mock_repository (MagicMock): A mock repository for purchase summary data.

    Asserts:
        - The average spending for the customer matches the price of the single product purchased.
    """
    # Test with one purchase
    mock_repository.purchase_summary.return_value = {
        customer_1: {product_1: 1}
    }
    result = service.calculate_avarage_spending_per_customer()
    assert result[customer_1] == product_1.price
    
def test_calculate_avarage_with_multiple_products(
        service: PurchasesSummaryService,
        customer_1: Customer,
        product_1: Product,
        product_2: Product,
        mock_repository: MagicMock) -> None:
    """
    Test the calculation of average spending when the customer has purchased multiple products.

    Args:
        service (PurchasesSummaryService): The service instance to test.
        customer_1 (Customer): A sample customer instance.
        product_1 (Product): The first sample product instance.
        product_2 (Product): The second sample product instance.
        mock_repository (MagicMock): A mock repository for purchase summary data.

    Asserts:
        - The average spending for the customer is calculated correctly based on the total price and quantity of products purchased.
    """
    # Test with multiple purchases
    mock_repository.purchase_summary.return_value = {
        customer_1: {
            product_1: 2, 
            product_2: 3}
    }
    result = service.calculate_avarage_spending_per_customer()
    expected_average = (product_1.total_price(2) + product_2.total_price(3)) / 5
    assert result[customer_1] == expected_average