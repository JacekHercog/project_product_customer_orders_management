from decimal import Decimal
from unittest.mock import MagicMock
from src.repository import PurchaseSummaryRepository, CustomersWithPurchesdProducts
from src.service import PurchasesSummaryService
from src.model import Customer, Product
import pytest

import logging
logging.basicConfig(level=logging.DEBUG)


def test_find_most_popular_product_with_no_purchases(
        service: PurchasesSummaryService,
        mock_repository: MagicMock) -> None:
    """
    Test finding the most popular products when there are no purchases.

    Args:
        service (PurchasesSummaryService): The service instance to test.
        mock_repository (MagicMock): A mock repository for purchase summary data.

    Asserts:
        - The result is an empty list when there are no purchases.
    """
    # Test with no purchases
    mock_repository.purchase_summary.return_value = {}
    result = service.find_most_popular_products()
    assert result == []

def test_find_most_popular_product_with_single_popular_product(
        service: PurchasesSummaryService,
        customer_1: Customer,
        customer_2: Customer,
        product_1: Product,
        product_2: Product,
        mock_repository: MagicMock) -> None:
    """
    Test finding the most popular product when there is a single most popular product.

    Args:
        service (PurchasesSummaryService): The service instance to test.
        customer_1 (Customer): A sample customer instance.
        customer_2 (Customer): Another sample customer instance.
        product_1 (Product): A sample product instance that is the most popular.
        product_2 (Product): Another sample product instance.
        mock_repository (MagicMock): A mock repository for purchase summary data.

    Asserts:
        - The result contains only the single most popular product.
        - The length of the result is 1.
    """
    # Test with a single popular product
    mock_repository.purchase_summary.return_value = {
        customer_1: {product_1: 3, product_2: 1},
        customer_2: {product_1: 2, product_2: 2}
    }
    result = service.find_most_popular_products()
    assert result == [product_1]
    assert len(result) == 1

def test_find_most_popular_product_with_multiple_popular_products(
        service: PurchasesSummaryService,
        customer_1: Customer,
        customer_2: Customer,
        product_1: Product,
        product_2: Product,
        mock_repository: MagicMock) -> None:
    """
    Test finding the most popular products when there are multiple equally popular products.

    Args:
        service (PurchasesSummaryService): The service instance to test.
        customer_1 (Customer): A sample customer instance.
        customer_2 (Customer): Another sample customer instance.
        product_1 (Product): A sample product instance that is one of the most popular.
        product_2 (Product): Another sample product instance that is equally popular.
        mock_repository (MagicMock): A mock repository for purchase summary data.

    Asserts:
        - The result contains all equally popular products.
        - The length of the result matches the number of equally popular products.
    """
    # Test with multiple popular products
    mock_repository.purchase_summary.return_value = {
        customer_1: {product_1: 3, product_2: 3},
        customer_2: {product_1: 2, product_2: 2}
    }
    result = service.find_most_popular_products()
    assert result == [product_1, product_2]
    assert len(result) == 2

