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
    Fixture to create a Customer object with ID 1.

    Returns:
        Customer: A customer instance with predefined attributes.
    """
    return Customer(id=1, first_name="John", last_name="Doe", age=30, email="john.doe@example.com")

@pytest.fixture
def customer_1_data() -> CustomerDataDict:
    """
    Fixture to create a dictionary representation of customer_1.

    Returns:
        CustomerDataDict: A dictionary containing customer_1's data.
    """
    return {
        "id": 1, "first_name": "John", "last_name": "Doe", "age": 30, "email": "john.doe@example.com"
    }

@pytest.fixture
def customer_2() -> Customer:
    """
    Fixture to create a Customer object with ID 2.

    Returns:
        Customer: A customer instance with predefined attributes.
    """
    return Customer(id=2, first_name="Jane", last_name="Doe", age=25, email="jane.doe@example.com")

@pytest.fixture
def customer_2_data() -> CustomerDataDict:
    """
    Fixture to create a dictionary representation of customer_2.

    Returns:
        CustomerDataDict: A dictionary containing customer_2's data.
    """
    return {
        "id": 2, "first_name": "Jane", "last_name": "Doe", "age": 25,"email": "jane.doe@example.com"
    }

@pytest.fixture
def product_1() -> Product:
    """
    Fixture to create a Product object with ID 101.

    Returns:
        Product: A product instance with predefined attributes.
    """
    return Product(id=101, name="Laptop", category=ProductCategory.ELECTRONICS, price=Decimal("1500.00"))

@pytest.fixture
def product_1_data() -> ProductDataDict:
    """
    Fixture to create a dictionary representation of product_1.

    Returns:
        ProductDataDict: A dictionary containing product_1's data.
    """
    return {"id": 101, "name": "Laptop", "category": "Electronics", "price": "1500.00"}

@pytest.fixture
def product_1_data_invalid() -> ProductDataDict:
    """
    Fixture to create an invalid dictionary representation of product_1.

    Returns:
        ProductDataDict: A dictionary missing required fields for product_1.
    """
    return {"id": 101, "name": "Laptop", "category": "Electronics"}  # type: ignore[typeddict-item]

@pytest.fixture
def product_2() -> Product:
    """
    Fixture to create a Product object with ID 102.

    Returns:
        Product: A product instance with predefined attributes.
    """
    return Product(id=102, name="T-Shirt", category=ProductCategory.CLOTHING, price=Decimal("20.00"))

@pytest.fixture
def product_2_data() -> ProductDataDict:
    """
    Fixture to create a dictionary representation of product_2.

    Returns:
        ProductDataDict: A dictionary containing product_2's data.
    """
    return {"id": 102, "name": "T-Shirt", "category": "Clothing", "price": "20.00"}

@pytest.fixture
def order_1() -> Order:
    """
    Fixture to create an Order object with ID 1.

    Returns:
        Order: An order instance with predefined attributes.
    """
    return Order(id=1, customer_id=1, product_id=101, quantity=2, discount=Decimal("0.1"),
                 shipping_method=ShippingMethod.STANDARD)

@pytest.fixture
def order_1_data() -> OrderDataDict:
    """
    Fixture to create a dictionary representation of order_1.

    Returns:
        OrderDataDict: A dictionary containing order_1's data.
    """
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
    """
    Fixture to create an Order object with ID 2.

    Returns:
        Order: An order instance with predefined attributes.
    """
    return Order(id=2, customer_id=1, product_id=102, quantity=5, discount=Decimal("0.0"),
                shipping_method=ShippingMethod.EXPRESS)

@pytest.fixture
def order_2_data() -> OrderDataDict:
    """
    Fixture to create a dictionary representation of order_2.

    Returns:
        OrderDataDict: A dictionary containing order_2's data.
    """
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
    """
    Fixture to create an Order object with ID 3.

    Returns:
        Order: An order instance with predefined attributes.
    """
    return Order(id=3, customer_id=2, product_id=101, quantity=1, discount=Decimal("0.2"),
                shipping_method=ShippingMethod.STANDARD)

@pytest.fixture
def order_3_data() -> OrderDataDict:
    """
    Fixture to create a dictionary representation of order_3.

    Returns:
        OrderDataDict: A dictionary containing order_3's data.
    """
    return {
        "id": 3, 
        "customer_id": 2, 
        "product_id": 101, 
        "quantity": 1, 
        "discount": "0.2",
        "shipping_method":"Standard"
    }