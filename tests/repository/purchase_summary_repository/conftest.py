import pytest
from unittest.mock import MagicMock
from src.model import (
    Product,
    Customer,
    Order,
    ProductDataDict,
    CustomerDataDict,
    OrderDataDict,
)
from src.repository import PurchaseSummaryRepository

@pytest.fixture
def mock_customer_repo(customer_1: Customer, customer_2: Customer) -> MagicMock:
    """
    Fixture for mocking the customer data repository.

    Args:
        customer_1 (Customer): A sample customer instance.
        customer_2 (Customer): Another sample customer instance.

    Returns:
        MagicMock: A mock repository with customer data.
    """
    mock_repo = MagicMock()
    mock_repo.get_data.return_value = [customer_1, customer_2]
    return mock_repo

@pytest.fixture
def mock_product_repo(product_1: Product, product_2: Product) -> MagicMock:
    """
    Fixture for mocking the product data repository.

    Args:
        product_1 (Product): A sample product instance.
        product_2 (Product): Another sample product instance.

    Returns:
        MagicMock: A mock repository with product data.
    """
    mock_repo = MagicMock()
    mock_repo.get_data.return_value = [product_1, product_2]
    return mock_repo

@pytest.fixture
def mock_order_repo(order_1: Order, order_2: Order, order_3: Order) -> MagicMock:
    """
    Fixture for mocking the order data repository.

    Args:
        order_1 (Order): A sample order instance.
        order_2 (Order): Another sample order instance.
        order_3 (Order): A third sample order instance.

    Returns:
        MagicMock: A mock repository with order data.
    """
    mock_repo = MagicMock()
    mock_repo.get_data.return_value = [order_1, order_2, order_3]
    return mock_repo

@pytest.fixture
def purchase_summary_repository(
    mock_customer_repo: MagicMock,
    mock_product_repo: MagicMock,
    mock_order_repo: MagicMock
) -> PurchaseSummaryRepository[CustomerDataDict, ProductDataDict, OrderDataDict]:
    """
    Fixture for creating a mocked PurchaseSummaryRepository instance.

    Args:
        mock_customer_repo (MagicMock): A mock repository for customer data.
        mock_product_repo (MagicMock): A mock repository for product data.
        mock_order_repo (MagicMock): A mock repository for order data.

    Returns:
        PurchaseSummaryRepository[CustomerDataDict, ProductDataDict, OrderDataDict]:
            A mocked instance of PurchaseSummaryRepository.
    """
    return PurchaseSummaryRepository[CustomerDataDict, ProductDataDict, OrderDataDict](
        customer_repo=mock_customer_repo,
        product_repo=mock_product_repo,
        order_repo=mock_order_repo
    )
