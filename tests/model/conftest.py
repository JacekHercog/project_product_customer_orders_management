from src.model import (
    Product,
    Customer,
    Order
)
import pytest

@pytest.fixture
def customers(customer_1: Customer, customer_2: Customer) -> list[Customer]:
    return [customer_1, customer_2]


@pytest.fixture
def products(product_1: Product, product_2: Product) -> list[Product]:
    return [product_1, product_2]


@pytest.fixture
def orders(order_1: Order, order_2: Order, order_3: Order) -> list[Order]:
    return [order_1, order_2, order_3]
