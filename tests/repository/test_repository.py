import pytest
from unittest.mock import MagicMock
from src.model import (
    Product, Customer, Order, ProductDataDict, CustomerDataDict, OrderDataDict,
    ProductCategory, ShippingMethod
)
from src.validator import ProductDataDictValidator, CustomerDataDictValidator, OrderDataDictValidator
from src.converter import ProductConverter, CustomerConverter, OrderConverter
from src.repository import ProductDataRepository, CustomerDataRepository, OrderDataRepository
from src.file_service import ProductJsonFileReader
from decimal import Decimal
from typing import cast
from pathlib import Path
import json

import logging

def test_get_data_empty_cache_logs_warning(
        product_data_repository: ProductDataRepository, 
        caplog: pytest.LogCaptureFixture
) -> None:
    
    with caplog.at_level(logging.WARNING):
        data = product_data_repository.get_data()
    assert "No data avialble in cache." in caplog.text
    assert len(data) == 0

def test_refresh_product_data_calls_file_reader_and_process_data(
        product_data_repository: ProductDataRepository, 
        file_reader_mock: MagicMock
) -> None:
   
    file_reader_mock.read.return_value = [
        {"id": 1, "name": "Product 1", "category": "Electronics", "price": 100.0}
    ]

    validator_mock = cast(MagicMock, product_data_repository.validator.validate)
    validator_mock.return_value = True

    converter_mock = cast(MagicMock, product_data_repository.converter.convert)
    converter_mock.return_value = Product(
        id=1, name="Product 1", category=ProductCategory.ELECTRONICS, price=Decimal("100.0")
    )

    data = product_data_repository.refresh_data()

    file_reader_mock.read.assert_called_with("products.json")
    assert file_reader_mock.read.call_count == 2
    assert len(data) == 1
    assert isinstance(data[0], Product)
    assert data[0].id == 1
    assert data[0].name == "Product 1"
    assert data[0].category == ProductCategory.ELECTRONICS
    assert data[0].price == Decimal("100.0")

def test_refresh_customer_data_calls_file_reader_and_process_data(
        customer_data_repository: CustomerDataRepository,
        file_reader_mock: MagicMock
) -> None:
    
    file_reader_mock.read.return_value = [
        {"id": 1, "first_name": "John","last_name": "Doe","age": 30, "email": "john.Doe@gmail.com"}
    ]
    customer_data_repository.validator = MagicMock()
    customer_data_repository.validator.validate.return_value = True

    customer_data_repository.converter = MagicMock()
    customer_data_repository.converter.convert.return_value = Customer(
        id=1, first_name="John", last_name="Doe",age=int(30),email = "john.Doe@gmail.com"
    )

    data = customer_data_repository.refresh_data()
    file_reader_mock.read.assert_called_with('customers.json')
    assert file_reader_mock.read.call_count == 2
    assert len(data) == 1
    assert isinstance(data[0], Customer)
    assert data[0].id == 1
    assert data[0].first_name == "John"
    assert data[0].last_name == "Doe"
    assert data[0].age == int(30)
    assert data[0].email == "john.Doe@gmail.com"

def test_refresh_customer_data_calls_file_reader_and_process_data_2(
        validator_mock: MagicMock,
        converter_mock: MagicMock,
        file_reader_mock: MagicMock
) -> None:
    
    file_reader_mock.read.return_value = [
        {"id": 1, "first_name": "A", "last_name": "AA", "age": 10, "email": "a@gmail.com"}]
    validator_mock.validate.return_value = True
    converter_mock.convert.return_value \
        = Customer(id=1, first_name="A", last_name="AA", age=10, email="a@gmail.com")

    customer_data_repository = CustomerDataRepository(
        file_reader=file_reader_mock,
        validator=validator_mock,
        converter=converter_mock,
        file_name='customers.json'
    )
    data = customer_data_repository.refresh_data()

    file_reader_mock.read.assert_called_with('customers.json')
    assert file_reader_mock.read.call_count == 2
    assert len(data) == 1
    assert data[0].id == 1
    assert data[0].first_name == "A"
    assert data[0].last_name == "AA"
    assert data[0].age == 10
    assert data[0].email == "a@gmail.com"

def test_invalid_entry_logs_error(
        product_data_repository: ProductDataRepository,
        file_reader_mock: MagicMock,
        validator_mock: MagicMock,
        converter_mock: MagicMock
) -> None:
    
    with pytest.raises(ValueError, match ='No filename set'):
        product_data_repository = ProductDataRepository(
            file_reader=file_reader_mock,
            validator=validator_mock,
            converter=converter_mock,
            file_name=None
        )

"""
Integration test
"""
def test_product_data_repository_with_real_json_file(tmp_path: Path) -> None:

    file_name = "tmp_products.json"
    test_file = tmp_path / file_name

    sample_data = [
        {
            "id": 1,
            "name": "Laptop",
            "category": "Electronics",
            "price": "999.99"
            },
        {
            "id": 2,
            "name": "Chair",
            "category": "Electronics",
            "price": "49.99"
        }
    ]

    product_1 = Product(
            id=1,
            name="Laptop",
            category=ProductCategory.ELECTRONICS,
            price=Decimal("999.99")
        )
    
    product_2 = Product(
            id=2,
            name="Chair",
            category=ProductCategory.ELECTRONICS,
            price=Decimal("49.99")
    )

    with open(test_file, 'w') as file:
        json.dump(sample_data, file)

    

    product_json_file_reader = ProductJsonFileReader()
    validator = ProductDataDictValidator()
    converter = ProductConverter()

    product_data_repository = ProductDataRepository(
        file_reader=product_json_file_reader,
        validator=validator,
        converter=converter,
        file_name=str(test_file)
    )

    data = product_data_repository.get_data()

    assert len(data) == 2
    assert data[0] == product_1
    assert data[1] == product_2
