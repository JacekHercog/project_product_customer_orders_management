import pytest
from unittest.mock import MagicMock
from src.model import (
    Product,
    Customer,
    Order
)
from src.repository import PurchaseSummaryRepository


@pytest.fixture
def mock_customer_repo(customer_1: Customer, customer_2: Customer) -> MagicMock:
    """
    Fixture for mocking the customer data repository.
    """
    mock_repo = MagicMock()
    mock_repo.get_data.return_value = [customer_1, customer_2]
    return mock_repo

@pytest.fixture
def mock_product_repo(product_1: Product, product_2: Product) -> MagicMock:
    """
    Fixture for mocking the product data repository.
    """
    mock_repo = MagicMock()
    mock_repo.get_data.return_value = [product_1, product_2]
    return mock_repo

@pytest.fixture
def mock_order_repo(order_1: Order, order_2: Order, order_3: Order) -> MagicMock:
    """
    Fixture for mocking the order data repository.
    """
    mock_repo = MagicMock()
    mock_repo.get_data.return_value = [order_1, order_2, order_3]
    return mock_repo

@pytest.fixture
def purchase_summary_repo(
    mock_customer_repo: MagicMock,
    mock_product_repo: MagicMock,
    mock_order_repo: MagicMock
) -> PurchaseSummaryRepository:
    """
    Fixture for mocking the data summary repository.
    """

    return PurchaseSummaryRepository(
        customer_repo=mock_customer_repo,
        product_repo=mock_product_repo,
        order_repo=mock_order_repo
    )
