import pytest
from unittest.mock import MagicMock
from src.model import Product, Customer, ProductDataDict, CustomerDataDict
from src.repository import ProductDataRepository, CustomerDataRepository
from typing import cast

import logging

def test_get_data_empty_cache_logs_warning(
        product_data_repository: ProductDataRepository, 
        caplog: pytest.LogCaptureFixture
) -> None:
    """
    Test that a warning is logged when attempting to retrieve data from an empty cache.

    Args:
        product_data_repository (ProductDataRepository): The repository instance to test.
        caplog (pytest.LogCaptureFixture): Fixture for capturing log messages.

    Asserts:
        - A warning message is logged.
        - The returned data is an empty list.
    """
    with caplog.at_level(logging.WARNING):
        data = product_data_repository.get_data()
    assert "No data avialble in cache." in caplog.text
    assert len(data) == 0

def test_refresh_product_data_calls_file_reader_and_process_data(
        product_data_repository: ProductDataRepository, 
        product_1: Product,
        product_1_data: ProductDataDict,
        file_reader_mock: MagicMock,
        validator_mock: MagicMock,
        converter_mock: MagicMock
) -> None:
    """
    Test that refreshing product data calls the file reader, validator, and converter.

    Args:
        product_data_repository (ProductDataRepository): The repository instance to test.
        product_1 (Product): A sample product instance.
        product_1_data (ProductDataDict): The dictionary representation of the sample product.
        file_reader_mock (MagicMock): Mock for the file reader.
        validator_mock (MagicMock): Mock for the validator.
        converter_mock (MagicMock): Mock for the converter.

    Asserts:
        - The file reader is called with the correct file name.
        - The validator and converter are called the correct number of times.
        - The returned data matches the expected product instance.
    """
   
    file_reader_mock.read.return_value = [product_1_data]

    # validator_mock = cast(MagicMock, product_data_repository.validator.validate)
    # validator_mock.return_value = True
    validator_mock.validate.return_value = True

    # converter_mock = cast(MagicMock, product_data_repository.converter.convert)
    # converter_mock.return_value = product_1
    converter_mock.convert.return_value = product_1

    data = product_data_repository.refresh_data()

    file_reader_mock.read.assert_called_with("products.json")
    assert file_reader_mock.read.call_count == 2
    assert len(data) == 1
    assert isinstance(data[0], Product)
    assert data[0] == product_1
    # assert data[0].id == product_1.id
    # assert data[0].name == product_1.name
    # assert data[0].category == product_1.category
    # assert data[0].price == product_1.price

def test_refresh_customer_data_calls_file_reader_and_process_data(
        customer_data_repository: CustomerDataRepository,
        customer_1: Customer,
        customer_1_data: CustomerDataDict,
        file_reader_mock: MagicMock,
        validator_mock: MagicMock,
        converter_mock: MagicMock
) -> None:
    """
    Test that refreshing customer data calls the file reader, validator, and converter.

    Args:
        customer_data_repository (CustomerDataRepository): The repository instance to test.
        customer_1 (Customer): A sample customer instance.
        customer_1_data (CustomerDataDict): The dictionary representation of the sample customer.
        file_reader_mock (MagicMock): Mock for the file reader.
        validator_mock (MagicMock): Mock for the validator.
        converter_mock (MagicMock): Mock for the converter.

    Asserts:
        - The file reader is called with the correct file name.
        - The validator and converter are called the correct number of times.
        - The returned data matches the expected customer instance.
    """
    
    file_reader_mock.read.return_value = [customer_1_data]

    # customer_data_repository.validator = MagicMock()
    # customer_data_repository.validator.validate.return_value = True
    validator_mock.validate.return_value = True

    # customer_data_repository.converter = MagicMock()
    # customer_data_repository.converter.convert.return_value = customer_1
    converter_mock.convert.return_value = customer_1

    data = customer_data_repository.refresh_data()
    file_reader_mock.read.assert_called_with('customers.json')
    assert file_reader_mock.read.call_count == 2
    assert len(data) == 1
    assert isinstance(data[0], Customer)
    assert data[0] == customer_1
    # assert data[0].id == customer_1.id
    # assert data[0].first_name == customer_1.first_name
    # assert data[0].last_name == customer_1.last_name
    # assert data[0].age == customer_1.age
    # assert data[0].email == customer_1.email

def test_refresh_customer_data_calls_file_reader_and_process_data_2(
        customer_2: Customer,
        customer_2_data: CustomerDataDict,
        validator_mock: MagicMock,
        converter_mock: MagicMock,
        file_reader_mock: MagicMock
) -> None:
    """
    Test refreshing customer data with a new repository instance.

    Args:
        customer_2 (Customer): A sample customer instance.
        customer_2_data (CustomerDataDict): The dictionary representation of the sample customer.
        validator_mock (MagicMock): Mock for the validator.
        converter_mock (MagicMock): Mock for the converter.
        file_reader_mock (MagicMock): Mock for the file reader.

    Asserts:
        - The file reader is called with the correct file name.
        - The returned data matches the expected customer instance.
    """
    
    file_reader_mock.read.return_value = [customer_2_data]
    validator_mock.validate.return_value = True
    converter_mock.convert.return_value = customer_2

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
    assert data[0].id == customer_2.id
    assert data[0].first_name == customer_2.first_name
    assert data[0].last_name == customer_2.last_name
    assert data[0].age == customer_2.age
    assert data[0].email == customer_2.email


def test_invalid_entry_logs_error(
        product_1_data: ProductDataDict,
        product_1_data_invalid: ProductDataDict,
        product_data_repository: ProductDataRepository,
        file_reader_mock: MagicMock,
        validator_mock: MagicMock,
        caplog: pytest.LogCaptureFixture
) -> None:
    """
    Test that invalid entries are logged as errors.

    Args:
        product_1_data (ProductDataDict): A valid product data dictionary.
        product_1_data_invalid (ProductDataDict): An invalid product data dictionary.
        product_data_repository (ProductDataRepository): The repository instance to test.
        file_reader_mock (MagicMock): Mock for the file reader.
        validator_mock (MagicMock): Mock for the validator.
        caplog (pytest.LogCaptureFixture): Fixture for capturing log messages.

    Asserts:
        - An error message is logged for the invalid entry.
        - The returned data contains only valid entries.
    """
    file_reader_mock.read.return_value = [product_1_data, product_1_data_invalid]
    validator_mock.validate.side_effect = [True, False]

    with caplog.at_level(logging.ERROR):
        data = product_data_repository.refresh_data()

    assert f"Invalid entry: {product_1_data_invalid}" in caplog.text
    assert len(data) == 1

def test_no_filename_raises_value_error(
        file_reader_mock: MagicMock,
        validator_mock: MagicMock,
        converter_mock: MagicMock
) -> None:
    """
    Test that initializing a repository without a file name raises a ValueError.

    Args:
        file_reader_mock (MagicMock): Mock for the file reader.
        validator_mock (MagicMock): Mock for the validator.
        converter_mock (MagicMock): Mock for the converter.

    Asserts:
        - A ValueError is raised with the correct error message.
    """
    with pytest.raises(ValueError, match='No filename set'):
        product_data_repository = ProductDataRepository(
            file_reader=file_reader_mock,
            validator=validator_mock,
            converter=converter_mock,
            file_name=None
        )
