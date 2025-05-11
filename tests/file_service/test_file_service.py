"""
Test suite for testing the functionality of file service classes.

This module contains tests for the following file service classes:
- `ProductJsonFileReader`: Reads product data from JSON files.
- `CustomerJsonFileReader`: Reads customer data from JSON files.
- `OrderJsonFileReader`: Reads order data from JSON files.
- `ProductJsonFileWriter`: Writes product data to JSON files.
- `CustomerJsonFileWriter`: Writes customer data to JSON files.
- `OrderJsonFileWriter`: Writes order data to JSON files.

Each test verifies that the file service classes correctly read and write data 
to and from JSON files.

Dependencies:
- `pytest`: Used for testing and fixture management.
- `src.file_service`: Contains the file service classes.
- `src.model`: Contains the data models (`ProductDataDict`, `CustomerDataDict`, `OrderDataDict`).
- `os`, `pathlib.Path`, `json`: Used for file operations.

Tests:
    - `test_file_service_init`: Verifies that the `ProductJsonFileReader` can be initialized.
    - `test_read_products`: Verifies that `ProductJsonFileReader` correctly reads product data from a JSON file.
    - `test_read_customers`: Verifies that `CustomerJsonFileReader` correctly reads customer data from a JSON file.
    - `test_read_orders`: Verifies that `OrderJsonFileReader` correctly reads order data from a JSON file.
    - `test_write_product`: Verifies that `ProductJsonFileWriter` correctly writes product data to a JSON file.
    - `test_write_customer`: Verifies that `CustomerJsonFileWriter` correctly writes customer data to a JSON file.
    - `test_write_order`: Verifies that `OrderJsonFileWriter` correctly writes order data to a JSON file.
"""

from src.file_service import (
    ProductJsonFileReader, 
    CustomerJsonFileReader, 
    OrderJsonFileReader,
    ProductJsonFileWriter,
    CustomerJsonFileWriter,
    OrderJsonFileWriter
)
from src.model import ProductDataDict, CustomerDataDict, OrderDataDict
import os
from pathlib import Path
import json

def test_file_service_init():
    """
    Test the initialization of `ProductJsonFileReader`.

    This test verifies that the `ProductJsonFileReader` can be initialized 
    and is an instance of the correct class.
    """
    file_service = ProductJsonFileReader()
    assert file_service is not None
    assert isinstance(file_service, ProductJsonFileReader)

def test_read_products(products_file: str, products_data: list[ProductDataDict]) -> None:
    """
    Test reading product data from a JSON file.

    This test verifies that `ProductJsonFileReader` correctly reads product data 
    from a JSON file and returns it as a list of dictionaries.

    Args:
        products_file (str): The path to the JSON file containing product data.
        products_data (list[ProductDataDict]): The expected product data.

    Assertions:
        - The data read from the file matches the expected product data.
        - The data is a list of dictionaries.
    """
    reader = ProductJsonFileReader()
    data = reader.read(products_file)
    assert data == products_data
    assert len(data) == 2
    assert data[0]['name'] == 'Laptop'
    assert isinstance(data, list)
    assert all(isinstance(item, dict) for item in data)

def test_read_customers(customers_file: str, customers_data: list[CustomerDataDict]) -> None:
    """
    Test reading customer data from a JSON file.

    This test verifies that `CustomerJsonFileReader` correctly reads customer data 
    from a JSON file and returns it as a list of dictionaries.

    Args:
        customers_file (str): The path to the JSON file containing customer data.
        customers_data (list[CustomerDataDict]): The expected customer data.

    Assertions:
        - The data read from the file matches the expected customer data.
        - The data is a list of dictionaries.
    """
    reader = CustomerJsonFileReader()
    data = reader.read(customers_file)
    assert data == customers_data
    assert len(data) == 2
    assert data[0]['first_name'] == 'John'
    assert isinstance(data, list)
    assert all(isinstance(item, dict) for item in data)

def test_read_orders(orders_file: str, orders_data: list[OrderDataDict]) -> None:
    """
    Test reading order data from a JSON file.

    This test verifies that `OrderJsonFileReader` correctly reads order data 
    from a JSON file and returns it as a list of dictionaries.

    Args:
        orders_file (str): The path to the JSON file containing order data.
        orders_data (list[OrderDataDict]): The expected order data.

    Assertions:
        - The data read from the file matches the expected order data.
        - The data is a list of dictionaries.
    """
    reader = OrderJsonFileReader()
    data = reader.read(orders_file)
    assert data == orders_data
    assert len(data) == 3
    assert data[0]['customer_id'] == 1
    assert isinstance(data, list)
    assert all(isinstance(item, dict) for item in data)

def test_write_product(tmpdir: Path, products_data: list[ProductDataDict]) -> None:
    """
    Test writing product data to a JSON file.

    This test verifies that `ProductJsonFileWriter` correctly writes product data 
    to a JSON file.

    Args:
        tmpdir (Path): A temporary directory provided by pytest.
        products_data (list[ProductDataDict]): The product data to write.

    Assertions:
        - The data written to the file matches the original product data.
    """
    writer = ProductJsonFileWriter()
    file_name = os.path.join(tmpdir, 'products_out.json')
    writer.write(file_name, products_data)

    with open(file_name, 'r', encoding='utf-8') as file:
        saved_data = json.load(file)
    
    assert saved_data == products_data

def test_write_customer(tmpdir: Path, customers_data: list[CustomerDataDict]) -> None:
    """
    Test writing customer data to a JSON file.

    This test verifies that `CustomerJsonFileWriter` correctly writes customer data 
    to a JSON file.

    Args:
        tmpdir (Path): A temporary directory provided by pytest.
        customers_data (list[CustomerDataDict]): The customer data to write.

    Assertions:
        - The data written to the file matches the original customer data.
    """
    writer = CustomerJsonFileWriter()
    file_name = os.path.join(tmpdir, 'customers_out.json')
    writer.write(file_name, customers_data)

    with open(file_name, 'r', encoding='utf-8') as file:
        saved_data = json.load(file)
    
    assert saved_data == customers_data

def test_write_order(tmpdir: Path, orders_data: list[OrderDataDict]) -> None:
    """
    Test writing order data to a JSON file.

    This test verifies that `OrderJsonFileWriter` correctly writes order data 
    to a JSON file.

    Args:
        tmpdir (Path): A temporary directory provided by pytest.
        orders_data (list[OrderDataDict]): The order data to write.

    Assertions:
        - The data written to the file matches the original order data.
    """
    writer = OrderJsonFileWriter()
    file_name = os.path.join(tmpdir, 'orders_out.json')
    writer.write(file_name, orders_data)

    with open(file_name, 'r', encoding='utf-8') as file:
        saved_data = json.load(file)
    
    assert saved_data == orders_data

