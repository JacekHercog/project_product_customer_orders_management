import pytest
from unittest.mock import MagicMock
from src.repository import (
    ProductDataRepository, CustomerDataRepository, OrderDataRepository
)

@pytest.fixture
def file_reader_mock() -> MagicMock:
    """
    Fixture for mocking the file reader.

    Returns:
        MagicMock: A mock object for the file reader.
    """
    return MagicMock()

@pytest.fixture
def validator_mock() -> MagicMock:
    """
    Fixture for mocking the validator.

    Returns:
        MagicMock: A mock object for the validator.
    """
    return MagicMock()

@pytest.fixture
def converter_mock() -> MagicMock:
    """
    Fixture for mocking the converter.

    Returns:
        MagicMock: A mock object for the converter.
    """
    return MagicMock()

@pytest.fixture
def product_data_repository(
    file_reader_mock: MagicMock, 
    validator_mock: MagicMock, 
    converter_mock: MagicMock
) -> ProductDataRepository:
    """
    Fixture for creating a ProductDataRepository instance.

    Args:
        file_reader_mock (MagicMock): A mock object for the file reader.
        validator_mock (MagicMock): A mock object for the validator.
        converter_mock (MagicMock): A mock object for the converter.

    Returns:
        ProductDataRepository: An instance of ProductDataRepository with mocked dependencies.
    """
    return ProductDataRepository(
        file_reader=file_reader_mock,
        validator=validator_mock,
        converter=converter_mock,
        file_name="products.json"
    )

@pytest.fixture
def customer_data_repository(
    file_reader_mock: MagicMock, 
    validator_mock: MagicMock, 
    converter_mock: MagicMock
) -> CustomerDataRepository:
    """
    Fixture for creating a CustomerDataRepository instance.

    Args:
        file_reader_mock (MagicMock): A mock object for the file reader.
        validator_mock (MagicMock): A mock object for the validator.
        converter_mock (MagicMock): A mock object for the converter.

    Returns:
        CustomerDataRepository: An instance of CustomerDataRepository with mocked dependencies.
    """
    return CustomerDataRepository(
        file_reader=file_reader_mock,
        validator=validator_mock,
        converter=converter_mock,
        file_name="customers.json"
    )

@pytest.fixture
def order_data_repository(
    file_reader_mock: MagicMock, 
    validator_mock: MagicMock, 
    converter_mock: MagicMock
) -> OrderDataRepository:
    """
    Fixture for creating an OrderDataRepository instance.

    Args:
        file_reader_mock (MagicMock): A mock object for the file reader.
        validator_mock (MagicMock): A mock object for the validator.
        converter_mock (MagicMock): A mock object for the converter.

    Returns:
        OrderDataRepository: An instance of OrderDataRepository with mocked dependencies.
    """
    return OrderDataRepository(
        file_reader=file_reader_mock,
        validator=validator_mock,
        converter=converter_mock,
        file_name="orders.json"
    )