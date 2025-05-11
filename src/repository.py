from abc import ABC
from dataclasses import dataclass, field
from collections import defaultdict
from src.file_service import FileReader
from src.validator import Validator
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
class DataRepository[T, U]:
    """
    Generic repository for managing data.

    Attributes:
        file_reader (FileReader[T]): The file reader used to read raw data.
        validator (Validator[T]): The validator used to validate raw data.
        converter (AbstractConverter[T, U]): The converter used to transform raw data into domain objects.
        file_name (str | None): The name of the file containing the data.
        _data (list[U]): Cached list of domain objects.

    Methods:
        get_data() -> list[U]:
            Retrieve cached data from the repository.
        refresh_data(file_name: str | None = None) -> list[U]:
            Refresh the data by re-reading and processing the file.
        _process_data(file_name: str) -> list[U]:
            Internal method to read, validate, and convert raw data.
    """
    file_reader: FileReader[T]
    validator: Validator[T]
    converter: AbstractConverter[T, U]
    file_name: str | None = None
    _data: list[U] = field(default_factory=list)
    
    def __post_init__(self) -> None:
        """
        Initialize the repository by loading data from the file.
        Raises:
            ValueError: If no file name is provided.
        """
        if self.file_name is None:
            raise ValueError("No filename set.")
        self._data = self.refresh_data(self.file_name)
   
    def get_data(self) -> list[U]:
        """
        Retrieve cached data from the repository.

        Returns:
            list[U]: A list of domain objects.
        """
        if not self._data:
            logging.warning("No data avialble in cache.")    
        return self._data

    
    def refresh_data(self, file_name: str | None = None) -> list[U]:
        """
        Refresh the data by re-reading and processing the file.

        Args:
            file_name (str | None): The name of the file to read. If None, the default file name is used.

        Returns:
            list[U]: A list of refreshed domain objects.
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
        Internal method to read, validate, and convert raw data.

        Args:
            file_name (str): The name of the file to process.

        Returns:
            list[U]: A list of validated and converted domain objects.
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

class ProductDataRepository(DataRepository[ProductDataDict, Product]):
    """
    Repository for managing product data.
    """
    pass

class CustomerDataRepository(DataRepository[CustomerDataDict, Customer]):
    """
    Repository for managing customer data.
    """
    pass

class OrderDataRepository(DataRepository[OrderDataDict, Order]):
    """
    Repository for managing order data.
    """
    pass


@dataclass
class PurchaseSummaryRepository[C, P, O]:
    """
    Repository for summarizing purchase data.

    Attributes:
        customer_repo (DataRepository[C, Customer]): Repository for customer data.
        product_repo (DataRepository[P, Product]): Repository for product data.
        order_repo (DataRepository[O, Order]): Repository for order data.
        _purchase_summary (CustomersWithPurchesdProducts): Cached summary of purchases.

    Methods:
        purchase_summary(forced_refreshed: bool = False) -> CustomersWithPurchesdProducts:
            Retrieve or refresh the purchase summary.
        _build_purchase_summary() -> CustomersWithPurchesdProducts:
            Internal method to build the purchase summary.
    """
    customer_repo: DataRepository[C, Customer]
    product_repo: DataRepository[P, Product]
    order_repo: DataRepository[O, Order]
    _purchase_summary: CustomersWithPurchesdProducts = field(default_factory=dict, init=False)

    def purchase_summary(self, forced_refreshed: bool = False) -> CustomersWithPurchesdProducts:
        """
        Retrieve or refresh the purchase summary.

        Args:
            forced_refreshed (bool): If True, forces a refresh of the summary.

        Returns:
            CustomersWithPurchesdProducts: A dictionary mapping customers to purchased products and quantities.
        """
        if forced_refreshed or not self._purchase_summary:
            logging.info("Building or refreshing purchase summary from repositories ...")
            self._purchase_summary = self._build_purchase_summary()
        return self._purchase_summary
    
    def _build_purchase_summary(self) -> CustomersWithPurchesdProducts: 
        """
        Internal method to build the purchase summary.

        Returns:
            CustomersWithPurchesdProducts: A dictionary mapping customers to purchased products and quantities.
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


