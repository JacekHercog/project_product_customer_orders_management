from decimal import Decimal
from unittest.mock import MagicMock
from src.repository import PurchaseSummaryRepository, CustomersWithPurchesdProducts
from src.service import PurchasesSummaryService
from src.model import Customer, Product
import pytest

import logging
logging.basicConfig(level=logging.DEBUG)


def test_find_highest_and_lowest_spenders_with_no_purchases(
        service: PurchasesSummaryService,
        mock_repository: MagicMock) -> None:
    """
    Test finding the highest and lowest spenders when there are no purchases.

    Args:
        service (PurchasesSummaryService): The service instance to test.
        mock_repository (MagicMock): A mock repository for purchase summary data.

    Asserts:
        - The result contains empty lists for both highest and lowest spenders.
    """
    # Test with no purchases
    mock_repository.purchase_summary.return_value = {}
    result = service.find_highest_and_lowest_spenders()
    assert result == ([], [])

def test_find_highest_and_lowest_spenders_with_different_spending(
        service: PurchasesSummaryService,
        customer_1: Customer,
        customer_2: Customer,
        product_1: Product,
        product_2: Product,
        mock_repository: MagicMock) -> None:
    """
    Test finding the highest and lowest spenders when customers have different spending amounts.

    Args:
        service (PurchasesSummaryService): The service instance to test.
        customer_1 (Customer): A sample customer instance with higher spending.
        customer_2 (Customer): A sample customer instance with lower spending.
        product_1 (Product): A sample product instance.
        product_2 (Product): Another sample product instance.
        mock_repository (MagicMock): A mock repository for purchase summary data.

    Asserts:
        - The result correctly identifies the highest and lowest spenders.
    """
    # Test with multiple customers
    mock_repository.purchase_summary.return_value = {
        customer_1: {product_1: 3},
        customer_2: {product_1: 1}
    }
    result = service.find_highest_and_lowest_spenders()
    assert result == ([customer_1], [customer_2])


def test_find_highest_and_lowest_spenders_with_multiple_highest_and_lowest(
        service: PurchasesSummaryService,
        customer_1: Customer,
        customer_2: Customer,
        product_1: Product,
        product_2: Product,
        mock_repository: MagicMock) -> None:
    """
    Test finding the highest and lowest spenders when multiple customers have the same spending amounts.

    Args:
        service (PurchasesSummaryService): The service instance to test.
        customer_1 (Customer): A sample customer instance.
        customer_2 (Customer): Another sample customer instance.
        product_1 (Product): A sample product instance.
        product_2 (Product): Another sample product instance.
        mock_repository (MagicMock): A mock repository for purchase summary data.

    Asserts:
        - The result correctly identifies multiple customers as both highest and lowest spenders.
    """
    # Test with multiple customers
    mock_repository.purchase_summary.return_value = {
        customer_1: {product_1: 3},
        customer_2: {product_1: 3}
    }
    result = service.find_highest_and_lowest_spenders()
    assert result == ([customer_1, customer_2], [customer_1, customer_2])
    # highest_spenders, lowest_spenders = service.find_highest_and_lowest_spenders()
    # assert highest_spenders == [customer_1, customer_2]
    # assert lowest_spenders == [customer_1, customer_2]


