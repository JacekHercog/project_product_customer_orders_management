from src.model import ProductDataDict, CustomerDataDict, OrderDataDict
import pytest
import os
import json

"""
Fixtures for testing file-based services.

This module provides pytest fixtures for generating test data and temporary files 
used in testing file-based services. The fixtures include data for products, customers, 
and orders, as well as temporary JSON files containing this data.

Fixtures:
    - `products_data`: Provides a list of product data dictionaries.
    - `customers_data`: Provides a list of customer data dictionaries.
    - `orders_data`: Provides a list of order data dictionaries.
    - `products_file`: Creates a temporary JSON file containing product data.
    - `customers_file`: Creates a temporary JSON file containing customer data.
    - `orders_file`: Creates a temporary JSON file containing order data.
"""

@pytest.fixture
def products_data(product_1_data: ProductDataDict, product_2_data: ProductDataDict) -> list[ProductDataDict]:
    """
    Fixture that provides a list of product data dictionaries.

    Args:
        product_1_data (ProductDataDict): Data for the first product.
        product_2_data (ProductDataDict): Data for the second product.

    Returns:
        list[ProductDataDict]: A list containing product data dictionaries.
    """
    return [product_1_data, product_2_data]

@pytest.fixture
def customers_data(customer_1_data: CustomerDataDict, customer_2_data: CustomerDataDict) -> list[CustomerDataDict]:
    """
    Fixture that provides a list of customer data dictionaries.

    Args:
        customer_1_data (CustomerDataDict): Data for the first customer.
        customer_2_data (CustomerDataDict): Data for the second customer.

    Returns:
        list[CustomerDataDict]: A list containing customer data dictionaries.
    """
    return [customer_1_data, customer_2_data]

@pytest.fixture
def orders_data(
    order_1_data: OrderDataDict, order_2_data: OrderDataDict, order_3_data: OrderDataDict) -> list[OrderDataDict]:
    """
    Fixture that provides a list of order data dictionaries.

    Args:
        order_1_data (OrderDataDict): Data for the first order.
        order_2_data (OrderDataDict): Data for the second order.
        order_3_data (OrderDataDict): Data for the third order.

    Returns:
        list[OrderDataDict]: A list containing order data dictionaries.
    """
    return [order_1_data, order_2_data, order_3_data]

@pytest.fixture
def products_file(tmpdir, products_data) -> str:
    """
    Fixture that creates a temporary JSON file containing product data.

    Args:
        tmpdir: A pytest-provided temporary directory.
        products_data (list[ProductDataDict]): A list of product data dictionaries.

    Returns:
        str: The path to the temporary JSON file containing product data.
    """
    file_path = os.path.join(tmpdir, "test_products.json")
    with open(file_path, "w") as file:
        json.dump(products_data, file)
    return file_path

@pytest.fixture
def customers_file(tmpdir, customers_data) -> str:
    """
    Fixture that creates a temporary JSON file containing customer data.

    Args:
        tmpdir: A pytest-provided temporary directory.
        customers_data (list[CustomerDataDict]): A list of customer data dictionaries.

    Returns:
        str: The path to the temporary JSON file containing customer data.
    """
    file_path = os.path.join(tmpdir, "test_customers.json")
    with open(file_path, "w") as file:
        json.dump(customers_data, file)
    return file_path

@pytest.fixture
def orders_file(tmpdir, orders_data) -> str:
    """
    Fixture that creates a temporary JSON file containing order data.

    Args:
        tmpdir: A pytest-provided temporary directory.
        orders_data (list[OrderDataDict]): A list of order data dictionaries.

    Returns:
        str: The path to the temporary JSON file containing order data.
    """
    file_path = os.path.join(tmpdir, "test_orders.json")
    with open(file_path, "w") as file:
        json.dump(orders_data, file)
    return file_path


