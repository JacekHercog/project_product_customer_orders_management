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
    file_service = ProductJsonFileReader()
    assert file_service is not None
    assert isinstance(file_service, ProductJsonFileReader)

def test_read_products(products_file: str, products_data : list[ProductDataDict]) -> None:
    reader = ProductJsonFileReader()
    data = reader.read(products_file)
    assert data == products_data
    assert len(data) == 2
    assert data[0]['name'] == 'Laptop'
    assert isinstance(data, list)
    assert all(isinstance(item, dict) for item in data)

def test_read_customers(customers_file: str, customers_data : list[CustomerDataDict]) -> None:
    reader = CustomerJsonFileReader()
    data = reader.read(customers_file)
    assert data == customers_data
    assert len(data) == 2
    assert data[0]['first_name'] == 'John'
    assert isinstance(data, list)
    assert all(isinstance(item, dict) for item in data)
   
def test_read_orders(orders_file: str, orders_data : list[OrderDataDict]) -> None:
    reader = OrderJsonFileReader()
    data = reader.read(orders_file)
    assert data == orders_data
    assert len(data) == 3
    assert data[0]['customer_id'] == 1 
    assert isinstance(data, list)
    assert all(isinstance(item, dict) for item in data)

def test_write_product(tmpdir: Path, products_data: list[ProductDataDict]) -> None:
    writer = ProductJsonFileWriter()
    file_name = os.path.join(tmpdir, 'products_out.json')
    writer.write(file_name, products_data)

    with open(file_name, 'r', encoding='utf-8') as file:
        saved_data = json.load(file)
    
    assert saved_data == products_data

def test_write_customer(tmpdir: Path, customers_data: list[CustomerDataDict]) -> None:
    writer = CustomerJsonFileWriter()
    file_name = os.path.join(tmpdir, 'customers_out.json')
    writer.write(file_name, customers_data)

    with open(file_name, 'r', encoding='utf-8') as file:
        saved_data = json.load(file)
    
    assert saved_data == customers_data

def test_write_order(tmpdir: Path, orders_data: list[OrderDataDict]) -> None:
    writer = OrderJsonFileWriter()
    file_name = os.path.join(tmpdir, 'orders_out.json')
    writer.write(file_name, orders_data)

    with open(file_name, 'r', encoding='utf-8') as file:
        saved_data = json.load(file)
    
    assert saved_data == orders_data
    
        