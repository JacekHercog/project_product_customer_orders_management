from abc import ABC, abstractmethod
from decimal import Decimal
from src.model import (ProductDataDict, CustomerDataDict, OrderDataDict, 
                       Product, Customer, Order,
                       ProductCategory, ShippingMethod)

class Converter[T, U](ABC):
    """
    Abstract base class for converters.
    """

    @abstractmethod
    def from_json(self, data: T) -> U:
        """
        Convert the data.
        """
        pass

class ProductConverter(Converter[ProductDataDict, Product]):
    """
    Converter for Product.
    """

    def from_json(self, data: ProductDataDict) -> Product:
        """
        Convert the JSON data to a Product object.
        """
        return Product(
            id= int(data["id"]),
            name= str(data["name"]),
            category=ProductCategory(str(data["category"])),
            price=Decimal(data["price"])
        )

   
class CustomerConverter(Converter[CustomerDataDict, Customer]):
    """
    Converter for Customer.
    """

    def from_json(self, data: CustomerDataDict) -> Customer:
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

class OrderConverter(Converter[OrderDataDict, Order]):
    """
    Converter for Order.
    """

    def from_json(self, data: OrderDataDict) -> Order:
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