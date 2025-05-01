import pytest
from src.model import (
    Product,
    Customer,
    Order,
    ProductCategory,
    ShippingMethod,
    CustomerDataDict,
    ProductDataDict,
    OrderDataDict
)
from decimal import Decimal

@pytest.fixture
def customer_1() -> Customer:
    """
    Fixture to create a Customer object with ID 1."""
    return Customer(id=1, first_name="John", last_name="Doe", age=30, email="john.doe@example.com")

@pytest.fixture
def customer_1_data() -> CustomerDataDict:
    return {
        "id": 1, "first_name": "John", "last_name": "Doe", "age": 30, "email": "john.doe@example.com"
    }

@pytest.fixture
def customer_2() -> Customer:
    return Customer(id=2, first_name="Jane", last_name="Doe", age=25, email="jane.doe@example.com")

@pytest.fixture
def customer_2_data() -> CustomerDataDict:
    return {
        "id": 2, "first_name": "Jane", "last_name": "Doe", "age": 25,"email": "jane.doe@example.com"
    }

@pytest.fixture
def product_1() -> Product:
    return Product(id=101, name="Laptop", category=ProductCategory.ELECTRONICS, price=Decimal("1500.00"))

@pytest.fixture
def product_1_data() -> ProductDataDict:
    return {"id": 101, "name": "Laptop", "category": "Electronics", "price": "1500.00"}

@pytest.fixture
def product_1_data_invalid() -> ProductDataDict:
    return {"id": 101, "name": "Laptop", "category": "Electronics"}

@pytest.fixture
def product_2() -> Product:
    return Product(id=102, name="T-Shirt", category=ProductCategory.CLOTHING, price=Decimal("20.00"))

@pytest.fixture
def product_2_data() -> ProductDataDict:
    return {"id": 102, "name": "T-Shirt", "category": "Clothing", "price": "20.00"}

@pytest.fixture
def order_1() -> Order:
    return Order(id=1, customer_id=1, product_id=101, quantity=2, discount=Decimal("0.1"),
                 shipping_method=ShippingMethod.STANDARD)

@pytest.fixture
def order_1_data() -> OrderDataDict:
    return {
            "id": 1, 
            "customer_id": 1, 
            "product_id": 101, 
            "quantity": 2, 
            "discount": "0.1",
            "shipping_method": "Standard"
    }

@pytest.fixture
def order_2() -> Order:
    return Order(id=2, customer_id=1, product_id=102, quantity=5, discount=Decimal("0.0"),
                shipping_method=ShippingMethod.EXPRESS)

@pytest.fixture
def order_2_data() -> OrderDataDict:
    return {
        "id": 2, 
        "customer_id": 1, 
        "product_id": 102, 
        "quantity":5, 
        "discount": "0.0",
        "shipping_method":"Express"
    }

@pytest.fixture
def order_3() -> Order:
    return Order(id=3, customer_id=2, product_id=101, quantity=1, discount=Decimal("0.2"),
                shipping_method=ShippingMethod.STANDARD)

@pytest.fixture
def order_3_data() -> OrderDataDict:
    return {
        "id": 3, 
        "customer_id": 2, 
        "product_id": 101, 
        "quantity": 1, 
        "discount": "0.2",
        "shipping_method":"Standard"
    }