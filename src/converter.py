from abc import ABC, abstractmethod
from decimal import Decimal
from src.model import (ProductDataDict, CustomerDataDict, OrderDataDict, 
                       Product, Customer, Order,
                       ProductCategory, ShippingMethod)

class AbstractConverter[T, U](ABC):
    """
    Abstract base class for converters.
    """

    @abstractmethod
    def convert(self, data: T) -> U:
        """
        Convert the data.
        """
        pass

class ProductConverter(AbstractConverter[ProductDataDict, Product]):
    """
    Converter for Product.
    """

    def convert(self, data: ProductDataDict) -> Product:
        """
        Convert the JSON data to a Product object.
        """
        return Product(
            id= int(data["id"]),
            name= str(data["name"]),
            category=ProductCategory(str(data["category"])),
            price=Decimal(data["price"])
        )

   
class CustomerConverter(AbstractConverter[CustomerDataDict, Customer]):
    """
    Converter for Customer.
    """

    def convert(self, data: CustomerDataDict) -> Customer:
        """
        Convert the JSON data to a Customer object.
        """
        return Customer(
            id= int(data["id"]),
            first_name= str(data["first_name"]),
            last_name= str(data["last_name"]),
            age= int(data["age"]),
            email= str(data["email"])   
        )

class OrderConverter(AbstractConverter[OrderDataDict, Order]):
    """
    Converter for Order.
    """

    def convert(self, data: OrderDataDict) -> Order:
        """
        Convert the JSON data to an Order object.
        """
        return Order(
            id= int(data["id"]),
            customer_id= int(data["customer_id"]),
            product_id= int(data["product_id"]),
            quantity= int(data["quantity"]),
            discount= Decimal(data["discount"]),
            shipping_method=ShippingMethod(str(data["shipping_method"]))
        )