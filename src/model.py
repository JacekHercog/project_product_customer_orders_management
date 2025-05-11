from dataclasses import dataclass
from decimal import Decimal
from typing import TypedDict
from enum import Enum

class ProductDataDict(TypedDict):
    """
    Typed dictionary for product data.

    Attributes:
        id (int): The unique identifier of the product.
        name (str): The name of the product.
        category (str): The category of the product.
        price (str): The price of the product as a string.
    """
    id: int
    name: str
    category: str
    price: str

class CustomerDataDict(TypedDict):
    """
    Typed dictionary for customer data.

    Attributes:
        id (int): The unique identifier of the customer.
        first_name (str): The first name of the customer.
        last_name (str): The last name of the customer.
        age (int): The age of the customer.
        email (str): The email address of the customer.
    """
    id: int
    first_name: str
    last_name: str
    age: int
    email: str

class OrderDataDict(TypedDict):
    """
    Typed dictionary for order data.

    Attributes:
        id (int): The unique identifier of the order.
        customer_id (int): The ID of the customer who placed the order.
        product_id (int): The ID of the product in the order.
        quantity (int): The quantity of the product ordered.
        discount (str): The discount applied to the order as a string.
        shipping_method (str): The shipping method for the order.
    """
    id: int
    customer_id: int
    product_id: int
    quantity: int
    discount: str
    shipping_method: str

class ProductCategory(Enum):
    """
    Enum representing product categories.

    Attributes:
        ELECTRONICS (str): Represents the electronics category.
        CLOTHING (str): Represents the clothing category.
        BOOKS (str): Represents the books category.
    """
    ELECTRONICS = "Electronics"
    CLOTHING = "Clothing"
    BOOKS = "Books"

class ShippingMethod(Enum):
    """
    Enum representing shipping methods.

    Attributes:
        STANDARD (str): Represents standard shipping.
        EXPRESS (str): Represents express shipping.
    """
    STANDARD = "Standard"
    EXPRESS = "Express"


@dataclass(frozen=True)
class Product:
    """
    Class representing a product.

    Attributes:
        id (int): The unique identifier of the product.
        name (str): The name of the product.
        category (ProductCategory): The category of the product.
        price (Decimal): The price of the product.

    Methods:
        total_price(quantity: int) -> Decimal:
            Calculate the total price for a given quantity of the product.
        to_dict() -> ProductDataDict:
            Convert the product instance to a dictionary.
    """
    id: int
    name: str
    category: ProductCategory
    price: Decimal

    def total_price(self, quantity: int) -> Decimal:
        """
        Calculate the total price for a given quantity.

        Args:
            quantity (int): The quantity of the product.

        Returns:
            Decimal: The total price for the given quantity.
        """
        return self.price * quantity

    def to_dict(self) -> ProductDataDict:
        """
        Convert the product to a dictionary.

        Returns:
            ProductDataDict: A dictionary representation of the product.
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

    Attributes:
        id (int): The unique identifier of the customer.
        first_name (str): The first name of the customer.
        last_name (str): The last name of the customer.
        age (int): The age of the customer.
        email (str): The email address of the customer.

    Methods:
        to_dict() -> CustomerDataDict:
            Convert the customer instance to a dictionary.
    """
    id: int
    first_name: str
    last_name: str
    age: int
    email: str
    
    def to_dict(self) -> CustomerDataDict:
        """
        Convert the customer to a dictionary.

        Returns:
            CustomerDataDict: A dictionary representation of the customer.
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

    Attributes:
        id (int): The unique identifier of the order.
        customer_id (int): The ID of the customer who placed the order.
        product_id (int): The ID of the product in the order.
        quantity (int): The quantity of the product ordered.
        discount (Decimal): The discount applied to the order.
        shipping_method (ShippingMethod): The shipping method for the order.

    Methods:
        to_dict() -> OrderDataDict:
            Convert the order instance to a dictionary.
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

        Returns:
            OrderDataDict: A dictionary representation of the order.
        """
        return {
            "id": self.id,
            "customer_id": self.customer_id,
            "product_id": self.product_id,
            "quantity": self.quantity,
            "discount": str(self.discount),
            "shipping_method": self.shipping_method.value
        }