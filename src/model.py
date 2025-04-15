from dataclasses import dataclass
from decimal import Decimal
from typing import Self
from enum import Enum

ProductDataDict = dict[str, str | int]
CustomerDataDict = dict[str, str | int]
OrderDataDict = dict[str, str | int]

class ProductCategory(Enum):
    """
    Enum representing product categories.
    """
    ELECTRONICS = "Electronics"
    CLOTHING = "Clothing"
    BOOKS = "Books"

class ShippingMethod(Enum):
    """
    Enum representing shipping methods.
    """
    STANDARD = "Standard"
    EXPRESS = "Express"


@dataclass(frozen=True)
class Product:
    """
    Class representing a product.
    """
    id: int
    name: str
    category: ProductCategory
    price: Decimal

    def to_dict(self) -> ProductDataDict:
        """
        Convert the product to a dictionary.
        """
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category.value,
            "price": str(self.price)
        }

@dataclass(frozen=True)
class Customer:
    """
    Class representing a customer.
    """
    id: int
    first_name: str
    last_name: str
    age: int
    email: str
    
    def to_dict(self) -> CustomerDataDict:
        """
        Convert the customer to a dictionary.
        """
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "email": self.email
        }
    

@dataclass
class Order:
    """
    Class representing an order.
    """
    id: int
    customer_id: int
    product_id: int
    quantity: int
    discount: Decimal
    shipping_method: ShippingMethod

    def to_dict(self) -> OrderDataDict:
        """
        Convert the order to a dictionary.
        """
        return {
            "id": self.id,
            "customer_id": self.customer_id,
            "product_id": self.product_id,
            "quantity": self.quantity,
            "discount": str(self.discount),
            "shipping_method": self.shipping_method.value
        }