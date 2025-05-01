from src.repository import PurchaseSummaryRepository, CustomersWithPurchesdProducts
from src.model import (Product, Customer, Order, ShippingMethod)
from decimal import Decimal
import pytest
from unittest.mock import MagicMock
import logging
from typing import cast

def test_initial_state_empty_cache(purchase_summary_repo: PurchaseSummaryRepository) -> None:
    """
    Test the initial state of the repository with an empty cache.
    """
    assert purchase_summary_repo._purchase_summary == {}

def test_purchase_summary_build_cache(
    purchase_summary_repo: PurchaseSummaryRepository,
    customer_1: Customer,
    customer_2: Customer,
    product_1: Product,
    product_2: Product
) -> None:
    """
    Test the build_cache method of the PurchaseSummaryRepository.
    """
    
    summary = purchase_summary_repo.purchase_summary()
    assert len(summary) == 2  
    
    cust_1 = summary.get(customer_1)
    assert cust_1 is not None
    assert cust_1.get(product_1) == 2   
    assert cust_1.get(product_2) == 5

    cust_2 = summary.get(customer_2)
    assert cust_2 is not None
    assert cust_2.get(product_1) == 1

def test_purchase_summary_cache_reuse(
    purchase_summary_repo: PurchaseSummaryRepository
) -> None:
    """
    Test the cache reuse of the PurchaseSummaryRepository.
    """
    
    summary = purchase_summary_repo.purchase_summary()
    assert len(summary) == 2 

    customer_repo_mock = MagicMock()
    customer_repo_mock = cast(MagicMock, purchase_summary_repo.customer_repo.get_data)
    customer_repo_mock.return_value.append(
        Customer(id=3, first_name="Alice", last_name="Smith", age=40, email="alice.smith@example.com")
    )

    summary_after_modification = purchase_summary_repo.purchase_summary()
    assert len(summary_after_modification) == 2
    assert summary_after_modification == summary

def test_purchase_summary_forced_refresh(
    purchase_summary_repo: PurchaseSummaryRepository,
    customer_1: Customer,
    product_1: Product
) -> None:
    """
    Test the forced refresh of the purchase summary.
    """
    
    _ = purchase_summary_repo.purchase_summary(forced_refreshed=True)
     

    new_order = Order(
        id=4,
        customer_id=1,
        product_id=101,
        quantity=3,
        discount=Decimal("0.05"),
        shipping_method=ShippingMethod.STANDARD
    )
    
    order_repo_mock = MagicMock()
    order_repo_mock = cast(MagicMock, purchase_summary_repo.order_repo.get_data)  
    order_repo_mock.return_value.append(new_order)

    summary = purchase_summary_repo.purchase_summary(forced_refreshed=True)
    assert summary[customer_1][product_1] == 5

def test_invalid_entry_logs_warning(
        purchase_summary_repo: PurchaseSummaryRepository,
        caplog: pytest.LogCaptureFixture
) -> None:
    """
    Test that invalid entries are logged as warnings.
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
    order_repo_mock = cast(MagicMock, purchase_summary_repo.order_repo.get_data)
    order_repo_mock.return_value.append(invalid_order)

    with caplog.at_level("WARNING"):
        _ = purchase_summary_repo.purchase_summary(forced_refreshed=True)  
        assert any(
            "invalid customer or product reference" in record.message
            for record in caplog.records
        )
    