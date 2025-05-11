from src.model import (
    Product,
    Customer,
    Order
)
import pytest

@pytest.fixture
def customers(customer_1: Customer, customer_2: Customer) -> list[Customer]:
    """
    Fixture providing a list of customer objects.

    Args:
        customer_1 (Customer): The first customer object.
        customer_2 (Customer): The second customer object.

    Returns:
        list[Customer]: A list containing the provided customer objects.
    """
    return [customer_1, customer_2]

@pytest.fixture
def products(product_1: Product, product_2: Product) -> list[Product]:
    """
    Fixture providing a list of product objects.

    Args:
        product_1 (Product): The first product object.
        product_2 (Product): The second product object.

    Returns:
        list[Product]: A list containing the provided product objects.
    """
    return [product_1, product_2]

@pytest.fixture
def orders(order_1: Order, order_2: Order, order_3: Order) -> list[Order]:
    """
    Fixture providing a list of order objects.

    Args:
        order_1 (Order): The first order object.
        order_2 (Order): The second order object.
        order_3 (Order): The third order object.

    Returns:
        list[Order]: A list containing the provided order objects.
    """
    return [order_1, order_2, order_3]
