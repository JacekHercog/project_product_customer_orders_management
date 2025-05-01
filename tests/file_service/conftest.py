from src.model import ProductDataDict, CustomerDataDict, OrderDataDict
import pytest
import os
import json

@pytest.fixture
def products_data(product_1_data: ProductDataDict, product_2_data: ProductDataDict) -> list[ProductDataDict]:
    return [product_1_data, product_2_data]

@pytest.fixture
def customers_data(customer_1_data: CustomerDataDict, customer_2_data: CustomerDataDict) -> list[CustomerDataDict]:
    return [customer_1_data, customer_2_data]

@pytest.fixture
def orders_data(
    order_1_data: OrderDataDict, order_2_data: OrderDataDict, order_3_data: OrderDataDict) -> list[OrderDataDict]:
    return [order_1_data, order_2_data, order_3_data]

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


