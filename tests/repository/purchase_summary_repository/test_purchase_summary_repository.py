from src.repository import PurchaseSummaryRepository, CustomersWithPurchesdProducts
from src.model import (
    Product,
    Customer, 
    Order, 
    ShippingMethod,
    CustomerDataDict,
    ProductDataDict,
    OrderDataDict
    )
from decimal import Decimal
import pytest
from unittest.mock import MagicMock
import logging
from typing import cast

def test_initial_state_empty_cache(
        purchase_summary_repository: PurchaseSummaryRepository[CustomerDataDict, ProductDataDict, OrderDataDict]
        ) -> None:
    """
    Test the initial state of the repository with an empty cache.

    Args:
        purchase_summary_repository (PurchaseSummaryRepository): The repository instance to test.

    Asserts:
        - The initial cache (`_purchase_summary`) is empty.
    """
    assert purchase_summary_repository._purchase_summary == {}

def test_purchase_summary_build_cache(
    purchase_summary_repository: PurchaseSummaryRepository[CustomerDataDict, ProductDataDict, OrderDataDict], 
    customer_1: Customer,
    customer_2: Customer,
    product_1: Product,
    product_2: Product
) -> None:
    """
    Test the `purchase_summary` method to ensure it builds the cache correctly.

    Args:
        purchase_summary_repository (PurchaseSummaryRepository): The repository instance to test.
        customer_1 (Customer): A sample customer instance.
        customer_2 (Customer): Another sample customer instance.
        product_1 (Product): A sample product instance.
        product_2 (Product): Another sample product instance.

    Asserts:
        - The summary contains the correct number of customers.
        - The product quantities for each customer are correct.
    """
    
    summary = purchase_summary_repository.purchase_summary()
    assert len(summary) == 2  
    
    cust_1 = summary.get(customer_1)
    assert cust_1 is not None
    assert cust_1.get(product_1) == 2   
    assert cust_1.get(product_2) == 5

    cust_2 = summary.get(customer_2)
    assert cust_2 is not None
    assert cust_2.get(product_1) == 1

def test_purchase_summary_cache_reuse(
    purchase_summary_repository: PurchaseSummaryRepository[CustomerDataDict, ProductDataDict, OrderDataDict]
    ) -> None:
    """
    Test that the cache is reused when the `purchase_summary` method is called without forcing a refresh.

    Args:
        purchase_summary_repository (PurchaseSummaryRepository): The repository instance to test.

    Asserts:
        - The cache is not modified after the first call to `purchase_summary`.
    """
    
    summary = purchase_summary_repository.purchase_summary()
    assert len(summary) == 2 

    customer_repo_mock = MagicMock()
    customer_repo_mock = cast(MagicMock, purchase_summary_repository.customer_repo.get_data)
    customer_repo_mock.return_value.append(
        Customer(id=3, first_name="Alice", last_name="Smith", age=40, email="alice.smith@example.com")
    )

    summary_after_modification = purchase_summary_repository.purchase_summary()
    assert len(summary_after_modification) == 2
    assert summary_after_modification == summary

def test_purchase_summary_forced_refresh(
    purchase_summary_repository: PurchaseSummaryRepository[CustomerDataDict, ProductDataDict, OrderDataDict],
    customer_1: Customer,
    product_1: Product
) -> None:
    """
    Test the forced refresh functionality of the `purchase_summary` method.

    Args:
        purchase_summary_repository (PurchaseSummaryRepository): The repository instance to test.
        customer_1 (Customer): A sample customer instance.
        product_1 (Product): A sample product instance.

    Asserts:
        - The summary is updated correctly after a forced refresh.
    """
    
    _ = purchase_summary_repository.purchase_summary(forced_refreshed=True)
     
    new_order = Order(
        id=4,
        customer_id=1,
        product_id=101,
        quantity=3,
        discount=Decimal("0.05"),
        shipping_method=ShippingMethod.STANDARD
    )
    
    order_repo_mock = MagicMock()
    order_repo_mock = cast(MagicMock, purchase_summary_repository.order_repo.get_data)  
    order_repo_mock.return_value.append(new_order)

    summary = purchase_summary_repository.purchase_summary(forced_refreshed=True)
    assert summary[customer_1][product_1] == 5

def test_invalid_entry_logs_warning(
        purchase_summary_repository: PurchaseSummaryRepository[CustomerDataDict, ProductDataDict, OrderDataDict],
        caplog: pytest.LogCaptureFixture
) -> None:
    """
    Test that invalid entries in the repository are logged as warnings.

    Args:
        purchase_summary_repository (PurchaseSummaryRepository): The repository instance to test.
        caplog (pytest.LogCaptureFixture): Fixture for capturing log messages.

    Asserts:
        - A warning message is logged for invalid entries.
    """
    
    invalid_order = Order(
        id=5,
        customer_id=99,  # Invalid customer ID
        product_id=999,   # Invalid product ID
        quantity=1,
        discount=Decimal("0.0"),
        shipping_method=ShippingMethod.STANDARD
    )
    
    order_repo_mock = MagicMock()
    order_repo_mock = cast(MagicMock, purchase_summary_repository.order_repo.get_data)
    order_repo_mock.return_value.append(invalid_order)

    with caplog.at_level("WARNING"):
        _ = purchase_summary_repository.purchase_summary(forced_refreshed=True)  
        assert any(
            "invalid customer or product reference" in record.message
            for record in caplog.records
        )
