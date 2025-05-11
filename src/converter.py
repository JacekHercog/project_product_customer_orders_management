from abc import ABC, abstractmethod
from decimal import Decimal
from src.model import (ProductDataDict, CustomerDataDict, OrderDataDict, 
                       Product, Customer, Order,
                       ProductCategory, ShippingMethod)

class AbstractConverter[T, U](ABC):
    """
    Abstract base class for converters.

    This class provides a blueprint for creating converter classes that transform 
    data of type `T` into objects of type `U`. It is designed to be subclassed, 
    and the `convert` method must be implemented in any subclass.

    Type Parameters:
        - T: The input data type that the converter will process.
        - U: The output data type that the converter will produce.

    Methods:
        - convert(data: T) -> U:
            Abstract method that must be implemented by subclasses to define 
            the logic for converting data of type `T` into objects of type `U`.

    Example Usage:
        To create a concrete converter, subclass `AbstractConverter` and implement 
        the `convert` method. For example:

        >>> from abc import ABC
        >>> from dataclasses import dataclass
        >>> from typing import Dict

        >>> @dataclass
        ... class ExampleData:
        ...     id: int
        ...     name: str

        >>> class ExampleConverter(AbstractConverter[Dict[str, str], ExampleData]):
        ...     def convert(self, data: Dict[str, str]) -> ExampleData:
        ...         return ExampleData(id=int(data["id"]), name=data["name"])

        >>> data = {"id": "1", "name": "Example"}
        >>> converter = ExampleConverter()
        >>> result = converter.convert(data)
        >>> print(result)
        ExampleData(id=1, name='Example')
    """

    @abstractmethod
    def convert(self, data: T) -> U:
        """
        Convert the data.

        This method must be implemented by subclasses to define the logic for 
        converting data of type `T` into objects of type `U`.

        Args:
            data (T): The input data to be converted.

        Returns:
            U: The converted object of type `U`.

        Raises:
            NotImplementedError: If the method is not implemented in a subclass.
        """
        pass

class ProductConverter(AbstractConverter[ProductDataDict, Product]):
    """
    A converter class responsible for transforming JSON-like dictionary data 
    into a `Product` object.

    This class implements the `AbstractConverter` interface, specifically 
    for converting `ProductDataDict` (a dictionary representation of a product) 
    into a `Product` object.

    Methods:
        - convert(data: ProductDataDict) -> Product:
            Converts a dictionary containing product data into a `Product` object.

    Example Usage:
        >>> product_data = {
        ...     "id": "101",
        ...     "name": "Laptop",
        ...     "category": "Electronics",
        ...     "price": "1500.00"
        ... }
        >>> converter = ProductConverter()
        >>> product = converter.convert(product_data)
        >>> print(product)
        Product(id=101, name='Laptop', category=<ProductCategory.ELECTRONICS: 'Electronics'>, price=Decimal('1500.00'))
    """

    def convert(self, data: ProductDataDict) -> Product:
        """
        Convert the JSON-like dictionary data into a `Product` object.

        Args:
            data (ProductDataDict): A dictionary containing the product data. 
                Expected keys:
                    - "id" (str or int): The product ID.
                    - "name" (str): The name of the product.
                    - "category" (str): The category of the product, which will 
                      be converted to a `ProductCategory` enum.
                    - "price" (str): The price of the product, which will be 
                      converted to a `Decimal`.

        Returns:
            Product: A `Product` object created from the provided dictionary.

        Raises:
            KeyError: If any of the required keys ("id", "name", "category", "price") 
                      are missing from the input dictionary.
            ValueError: If the `category` value cannot be converted to a `ProductCategory` enum.

        Example:
            >>> product_data = {
            ...     "id": "101",
            ...     "name": "Laptop",
            ...     "category": "Electronics",
            ...     "price": "1500.00"
            ... }
            >>> converter = ProductConverter()
            >>> product = converter.convert(product_data)
            >>> print(product)
            Product(id=101, name='Laptop', category=<ProductCategory.ELECTRONICS: 'Electronics'>, price=Decimal('1500.00'))
        """
        return Product(
            id= data["id"],
            name= data["name"],
            category=ProductCategory(data["category"]),
            price=Decimal(data["price"])
        )

   
class CustomerConverter(AbstractConverter[CustomerDataDict, Customer]):
    """
    A converter class responsible for transforming JSON-like dictionary data 
    into a `Customer` object.

    This class implements the `AbstractConverter` interface, specifically 
    for converting `CustomerDataDict` (a dictionary representation of a customer) 
    into a `Customer` object.

    Methods:
        - convert(data: CustomerDataDict) -> Customer:
            Converts a dictionary containing customer data into a `Customer` object.

    Example Usage:
        >>> customer_data = {
        ...     "id": "1",
        ...     "first_name": "John",
        ...     "last_name": "Doe",
        ...     "age": "30",
        ...     "email": "john.doe@example.com"
        ... }
        >>> converter = CustomerConverter()
        >>> customer = converter.convert(customer_data)
        >>> print(customer)
        Customer(id=1, first_name='John', last_name='Doe', age=30, email='john.doe@example.com')
    """

    def convert(self, data: CustomerDataDict) -> Customer:
        """
        Convert the JSON-like dictionary data into a `Customer` object.

        Args:
            data (CustomerDataDict): A dictionary containing the customer data. 
                Expected keys:
                    - "id" (str or int): The customer ID.
                    - "first_name" (str): The first name of the customer.
                    - "last_name" (str): The last name of the customer.
                    - "age" (str or int): The age of the customer.
                    - "email" (str): The email address of the customer.

        Returns:
            Customer: A `Customer` object created from the provided dictionary.

        Raises:
            KeyError: If any of the required keys ("id", "first_name", "last_name", "age", "email") 
                      are missing from the input dictionary.

        Example:
            >>> customer_data = {
            ...     "id": "1",
            ...     "first_name": "John",
            ...     "last_name": "Doe",
            ...     "age": "30",
            ...     "email": "john.doe@example.com"
            ... }
            >>> converter = CustomerConverter()
            >>> customer = converter.convert(customer_data)
            >>> print(customer)
            Customer(id=1, first_name='John', last_name='Doe', age=30, email='john.doe@example.com')
        """
        return Customer(
            id= data["id"],
            first_name= data["first_name"],
            last_name= data["last_name"],
            age= data["age"],
            email= data["email"]   
        )

class OrderConverter(AbstractConverter[OrderDataDict, Order]):
    """
    A converter class responsible for transforming JSON-like dictionary data 
    into an `Order` object.

    This class implements the `AbstractConverter` interface, specifically 
    for converting `OrderDataDict` (a dictionary representation of an order) 
    into an `Order` object.

    Methods:
        - convert(data: OrderDataDict) -> Order:
            Converts a dictionary containing order data into an `Order` object.

    Example Usage:
        >>> order_data = {
        ...     "id": "1001",
        ...     "customer_id": "1",
        ...     "product_id": "101",
        ...     "quantity": "2",
        ...     "discount": "0.10",
        ...     "shipping_method": "Standard"
        ... }
        >>> converter = OrderConverter()
        >>> order = converter.convert(order_data)
        >>> print(order)
        Order(id=1001, customer_id=1, product_id=101, quantity=2, discount=Decimal('0.10'), shipping_method=<ShippingMethod.STANDARD: 'Standard'>)
    """

    def convert(self, data: OrderDataDict) -> Order:
        """
        Convert the JSON-like dictionary data into an `Order` object.

        Args:
            data (OrderDataDict): A dictionary containing the order data. 
                Expected keys:
                    - "id" (str or int): The order ID.
                    - "customer_id" (str or int): The ID of the customer who placed the order.
                    - "product_id" (str or int): The ID of the product being ordered.
                    - "quantity" (str or int): The quantity of the product ordered.
                    - "discount" (str): The discount applied to the order, which will 
                      be converted to a `Decimal`.
                    - "shipping_method" (str): The shipping method for the order, which will 
                      be converted to a `ShippingMethod` enum.

        Returns:
            Order: An `Order` object created from the provided dictionary.

        Raises:
            KeyError: If any of the required keys ("id", "customer_id", "product_id", "quantity", "discount", "shipping_method") 
                      are missing from the input dictionary.
            ValueError: If the `shipping_method` value cannot be converted to a `ShippingMethod` enum.

        Example:
            >>> order_data = {
            ...     "id": "1001",
            ...     "customer_id": "1",
            ...     "product_id": "101",
            ...     "quantity": "2",
            ...     "discount": "0.10",
            ...     "shipping_method": "Standard"
            ... }
            >>> converter = OrderConverter()
            >>> order = converter.convert(order_data)
            >>> print(order)
            Order(id=1001, customer_id=1, product_id=101, quantity=2, discount=Decimal('0.10'), shipping_method=<ShippingMethod.STANDARD: 'Standard'>)
        """
        return Order(
            id= data["id"],
            customer_id= data["customer_id"],
            product_id= data["product_id"],
            quantity= data["quantity"],
            discount= Decimal(data["discount"]),
            shipping_method=ShippingMethod(data["shipping_method"])
        )