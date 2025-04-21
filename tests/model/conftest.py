from decimal import Decimal
from src.model import (
    Product,
    Customer,
    Order,
    ProductCategory,
    ShippingMethod
)
import pytest

@pytest.fixture
def customer1() -> Customer:
    return Customer(id=1, first_name='Alice', last_name='Smith', age= 30, email='alice.smith@example.com')

@pytest.fixture
def customer2() -> Customer:
    return Customer(id=2, first_name='Bob', last_name='Johnson', age= 45, email='bob.johnson@example.com')

@pytest.fixture
def customer3() -> Customer:
    return Customer(id=2, first_name='Charlie', last_name='Brown', age= 28, email='charlie.brown@example.com')

@pytest.fixture
def customers(customer1, customer2, customer3) -> list[Customer]:
    return [customer1, customer2, customer3]

@pytest.fixture
def product1() -> Product:
    return Product(id=1, name='Laptop', category=ProductCategory.ELECTRONICS, price=Decimal('1500.00'))

@pytest.fixture
def product2() -> Product:
    return Product(id=2, name='Smartphone', category=ProductCategory.ELECTRONICS, price=Decimal('800.00'))

@pytest.fixture
def product3() -> Product:
    return Product(id=3, name='Book', category=ProductCategory.BOOKS, price=Decimal('20.00'))

@pytest.fixture
def products(product1, product2, product3) -> list[Product]:
    return [product1, product2, product3]

@pytest.fixture
def order1(customers, products) -> Order:
    return Order(
        id=1,
        customer_id=customers[0].id,
        product_id=products[0].id,
        quantity=2,
        discount= Decimal('0.10'),
        shipping_method=ShippingMethod.STANDARD
    )

@pytest.fixture
def order2(customers, products) -> Order:
    return Order(
        id=2,
        customer_id=customers[1].id,
        product_id=products[1].id,
        quantity=1,
        discount=Decimal('0.05'),
        shipping_method=ShippingMethod.EXPRESS
    )

@pytest.fixture
def order3(customers, products) -> Order:
    return Order(
        id=3,
        customer_id=customers[2].id,
        product_id=products[2].id,
        quantity=5,
        discount=Decimal('0.00'),
        shipping_method=ShippingMethod.STANDARD
    )

@pytest.fixture
def orders(order1, order2, order3) -> list[Order]:
    return [order1, order2, order3]
