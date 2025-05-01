from abc import ABC
from dataclasses import dataclass, field
from collections import defaultdict
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

CustomersWithPurchesdProducts = dict[Customer, dict[Product, int]]

@dataclass
class AbstractDataRepository[T, U](ABC):
    """
    Abstract base class for repositories.
    """
    file_reader: AbstractFileReader[T]
    validator: AbstractValidator[T]
    converter: AbstractConverter[T, U]
    file_name: str | None = None
    _data: list[U] = field(default_factory=list)
    
    def __post_init__(self) -> None:
        """
        Initialize the repository.
        """
        if self.file_name is None:
            raise ValueError("No filename set.")
        self._data = self.refresh_data(self.file_name)
   
    def get_data(self) -> list[U]:
        """
        Get data from the repository.
        """
        if not self._data:
            logging.warning("No data avialble in cache.")    
        return self._data

    
    def refresh_data(self, file_name: str | None = None) -> list[U]:
        """
        Refresh data in the repository.
        """
        if file_name is None:
            logging.warning("No filename provided. Using the default filename.")
        else:
            self.file_name = file_name

        logging.info(f"Refreshing data from {self.file_name}...")
        self._data = self._process_data(str(self.file_name))
        return self._data

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


@dataclass
class PurchaseSummaryRepository[C, P, O]:
    """
    Class for summarizing data.
    """
    customer_repo: AbstractDataRepository[C, Customer]
    product_repo: AbstractDataRepository[P, Product]
    order_repo: AbstractDataRepository[O, Order]
    _purchase_summary: CustomersWithPurchesdProducts = field(default_factory=dict, init=False)

    def purchase_summary(self, forced_refreshed: bool = False) -> CustomersWithPurchesdProducts:
        """
        Get purchase summary.
        """
        if forced_refreshed or not self._purchase_summary:
            logging.info("Building or refreshing purchase summary from repositories ...")
            self._purchase_summary = self._build_purchase_summary()
        return self._purchase_summary
    
    def _build_purchase_summary(self) -> CustomersWithPurchesdProducts: 
        """
        Build purchase summary.
        """
        purchase_summary: CustomersWithPurchesdProducts = defaultdict(lambda: defaultdict(int))
        # Get data from repositories
        customers = {customer.id: customer for customer in self.customer_repo.get_data()}
        products = {product.id: product for product in self.product_repo.get_data()}
        orders = self.order_repo.get_data()

        for order in orders:
            customer = customers.get(order.customer_id)
            product = products.get(order.product_id)
            if customer and product:
                purchase_summary[customer][product] += order.quantity
            else:
                logging.warning(f"Order {order.id} has invalid customer or product reference.")
        return dict(purchase_summary)

       
       