from src.model import ProductDataDict, CustomerDataDict, OrderDataDict
import pytest
import os
import json


@pytest.fixture
def products_data() -> list[ProductDataDict]:
    return[
        {"id": 1, "name": "Product A", "category": "Electronics", "price": "100"},
        {"id": 2, "name": "Product B", "category": "Electronics", "price": "200"},
    ]

@pytest.fixture
def customers_data() -> list[CustomerDataDict]:
    return [
        {"id": 1, "first_name": "Person A", "last_name": "AA", "age": 30, "email": "personA@example.com"},
        {"id": 2, "first_name": "Person B", "last_name": "BB", "age": 40, "email": "personB!@example.com"}
    ]

@pytest.fixture
def orders_data() -> list[OrderDataDict]:
    return [
        {"id": 1, "customer_id": 1, "product_id": 1, "quantity": 2, "discount": "0.1", "shipping_method": "Standard"},
        {"id": 2, "customer_id": 2, "product_id": 2, "quantity": 3, "discount": "0.2", "shipping_method": "Standard"},
    ]

@pytest.fixture
def products_file(tmpdir, products_data) -> str:
    file_path = os.path.join(tmpdir, "test_products.json")
    with open(file_path, "w") as file:
        json.dump(products_data, file)
    return file_path

@pytest.fixture
def customers_file(tmpdir, customers_data) -> str:
    file_path = os.path.join(tmpdir, "test_customers.json")
    with open(file_path, "w") as file:
        json.dump(customers_data, file)
    return file_path

@pytest.fixture
def orders_file(tmpdir, orders_data) -> str:
    file_path = os.path.join(tmpdir, "test_orders.json")
    with open(file_path, "w") as file:
        json.dump(orders_data, file)
    return file_path


