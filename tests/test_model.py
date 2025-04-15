import pytest
from decimal import Decimal
from src.model import (
    Product,
    Customer,
    Order,
    ProductCategory,
    ShippingMethod,
    CustomerDataDict
)

def test_product_to_dict(product1) -> None:
    data = product1.to_dict()
    expected_dict = {
        "id": 1,
        "name": "Laptop",
        "category": 'Electronics',
        "price": str(Decimal('1500.00'))
    }
    assert data == expected_dict

def test_customer_to_dict(customer1) -> None:
    data= customer1.to_dict()
    excepted_dict = {
        "id": 1,
        "first_name": "Alice",
        "last_name": "Smith",
        "age": 30,
        "email":'alice.smith@example.com'
    }
    assert data == excepted_dict

def test_order_to_dict(order1) -> None:
    data = order1.to_dict()
    expected_dict = {
        "id": 1,
        "product_id": 1,
        "customer_id": 1,
        "quantity": 2,
        "discount": str(Decimal('0.10')),
        "shipping_method": 'Standard'
    }
    assert data == expected_dict

