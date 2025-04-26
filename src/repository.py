from abc import ABC
from dataclasses import dataclass, field
from src.file_service import AbstractFileReader
from src.validator import AbstractValidator
from src.converter import AbstractConverter
from src.model import (
    ProductDataDict,
    CustomerDataDict,
    OrderDataDict,
    Product,
    Customer,
    Order
)
import logging

logging.basicConfig(level=logging.INFO)

@dataclass
class AbstractDataRepository[T, U](ABC):
    """
    Abstract base class for repositories.
    """
    file_reader: AbstractFileReader[T]
    validator: AbstractValidator[T]
    converter: AbstractConverter[T, U]
    file_name: str | None = None
    data: list[U] = field(default_factory=list)
    
    def __post_init__(self) -> None:
        """
        Initialize the repository.
        """
        if self.file_name is None:
            raise ValueError("No filename set.")
        self.data = self.refresh_data(self.file_name)
   
    def get_data(self) -> list[U]:
        """
        Get data from the repository.
        """
        if not self.data:
            logging.warning("No data avialble in cache.")    
        return self.data

    
    def refresh_data(self, file_name: str | None = None) -> list[U]:
        """
        Refresh data in the repository.
        """
        if file_name is None:
            logging.warning("No filename provided. Using the default filename.")
        else:
            self.file_name = file_name

        logging.info(f"Refreshing data from {self.file_name}...")
        self.data = self._process_data(str(self.file_name))
        return self.data

    def _process_data(self, file_name: str) -> list[U]:
        """
        Process the data.
        """
        logging.info(f"Reading data from {file_name}...")
        row_data = self.file_reader.read(file_name)
        valid_data = []
        for entry in row_data:
            if self.validator.validate(entry):
                converted_data = self.converter.convert(entry)
                valid_data.append(converted_data)
            else:   
                logging.error(f"Invalid entry: {entry}")
        return valid_data

class ProductDataRepository(AbstractDataRepository[ProductDataDict, Product]):
    """
    Repository for Product.
    """
    pass

class CustomerDataRepository(AbstractDataRepository[CustomerDataDict, Customer]):
    """
    Repository for Customer.
    """
    pass

class OrderDataRepository(AbstractDataRepository[OrderDataDict, Order]):
    """
    Repository for Order.
    """
    pass

       