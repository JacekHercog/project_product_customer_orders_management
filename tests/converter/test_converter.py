import pytest
from src.model import (
    ProductDataDict, CustomerDataDict, OrderDataDict, 
    ProductCategory, ShippingMethod, Product, Customer, Order
)
from src.converter import ProductConverter, CustomerConverter, OrderConverter
from decimal import Decimal

@pytest.mark.parametrize("data, product", [
    (
        {
            "id": 1,
            "name": "Laptop",
            "category": "Electronics",
            "price": 999.99
        },
        Product(
            id=1,
            name="Laptop",
            category=ProductCategory.ELECTRONICS,
            price=Decimal("999.99")
        )
    ),
    (
        {
            "id": 2,
            "name": "Chair",
            "category": "Electronics",
            "price": 49.99
        },
        Product(
            id=2,
            name="Chair",
            category=ProductCategory.ELECTRONICS,
            price=Decimal("49.99")
        )
    )
])
def test_product_converter(data: ProductDataDict, product: Product) -> None:
    converter = ProductConverter()
    converted_product = converter.convert(data)
    assert isinstance(converted_product, Product)
    assert converted_product.id == product.id
    assert converted_product.name == product.name
    assert converted_product.category == product.category
    assert converted_product.price.quantize(Decimal("0.01")) == product.price

@pytest.mark.parametrize("data, customer", [
    (
        {
            "id": 1,
            "first_name": "John",
            "last_name": "Doe",
            "age": 30,  
            "email": "john.Doe@gmail.com"
        },
        Customer(
            id=1,
            first_name="John",
            last_name="Doe",
            age=int(30),
            email = "john.Doe@gmail.com"
        )  
    )
])

def test_customer_converter(data:CustomerDataDict, customer: Customer) -> None:
    converter = CustomerConverter()
    converted_customers = converter.convert(data)
    assert isinstance(converted_customers, Customer)
    assert converted_customers  == customer
    assert converted_customers.id == customer.id        

@pytest.mark.parametrize("data, order", [
    (
        {
            "id": 1,
            "customer_id": 1,
            "product_id": 2,
            "quantity": 1,
            "discount": 0.1,
            "shipping_method": "Standard"
        },
        Order(
            id=1,
            customer_id=1,
            product_id=2,
            quantity=1,
            discount=Decimal("0.10"),
            shipping_method=ShippingMethod.STANDARD
        )
    ),
    (
        {
            "id": 2,
            "customer_id": 2,
            "product_id": 1,
            "quantity": 2,
            "discount": 0.2,
            "shipping_method": "Express"
        },
        Order(
            id=2,
            customer_id=2,
            product_id=1,
            quantity=2,
            discount=Decimal("0.20"),
            shipping_method=ShippingMethod.EXPRESS
        )
    )
])
def test_order_converter(data: OrderDataDict, order: Order) -> None:
    converter = OrderConverter()
    converted_orders = converter.convert(data)
    assert isinstance(converted_orders, Order)
    assert converted_orders.id == order.id
    assert converted_orders.customer_id == order.customer_id
    assert converted_orders.product_id == order.product_id
    assert converted_orders.quantity == order.quantity
    assert converted_orders.discount.quantize(Decimal("0.01")) == order.discount