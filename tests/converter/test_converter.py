import pytest
from pytest import FixtureRequest
from src.model import (Product, Customer, Order)
from src.converter import ProductConverter, CustomerConverter, OrderConverter
from decimal import Decimal

@pytest.mark.parametrize("product_data_fixture_name, product_fixture_name", [
    ("product_1_data","product_1"),
    ("product_2_data", "product_2")
])
def test_product_converter(product_data_fixture_name: str, product_fixture_name: str, request: FixtureRequest) -> None:
    converter = ProductConverter()
    data = request.getfixturevalue(product_data_fixture_name)
    converted_product = converter.convert(data)
    product = request.getfixturevalue(product_fixture_name)
    assert isinstance(converted_product, Product)
    assert converted_product.id == product.id
    assert converted_product.name == product.name
    assert converted_product.category == product.category
    assert converted_product.price.quantize(Decimal("0.01")) == product.price


@pytest.mark.parametrize("customer_data_fixture_name, customer_fixture_name", [
    ("customer_1_data","customer_1"),
    ("customer_2_data", "customer_2")
])

def test_customer_converter(customer_data_fixture_name:str, customer_fixture_name: str, request: FixtureRequest) -> None:
    converter = CustomerConverter()
    data = request.getfixturevalue(customer_data_fixture_name)
    converted_customers = converter.convert(data)
    customer = request.getfixturevalue(customer_fixture_name)
    assert isinstance(converted_customers, Customer)
    assert converted_customers  == customer
    assert converted_customers.id == customer.id        

@pytest.mark.parametrize("order_data_fixture_name, order_fixture_name", [
    ("order_1_data", "order_1"),
    ("order_2_data", "order_2"),
    ("order_3_data", "order_3" )
])
def test_order_converter(order_data_fixture_name: str, order_fixture_name: str, request: FixtureRequest) -> None:
    converter = OrderConverter()
    data= request.getfixturevalue(order_data_fixture_name)
    converted_orders = converter.convert(data)
    order = request.getfixturevalue(order_fixture_name)
    assert isinstance(converted_orders, Order)
    assert converted_orders.id == order.id
    assert converted_orders.customer_id == order.customer_id
    assert converted_orders.product_id == order.product_id
    assert converted_orders.quantity == order.quantity
    assert converted_orders.discount.quantize(Decimal("0.01")) == order.discount