from src.model import (
    Product,
    Customer,
    Order,
    ProductDataDict,
    CustomerDataDict,
    OrderDataDict
)

def test_product_to_dict(product_1: Product, product_1_data: ProductDataDict ) -> None:
    data = product_1.to_dict()
    excepted_dict = product_1_data
    assert data == excepted_dict

def test_customer_to_dict(customer_1: Customer, customer_1_data: CustomerDataDict) -> None:
    data= customer_1.to_dict()
    excepted_dict = customer_1_data
    assert data == excepted_dict

def test_order_to_dict(order_1: Order, order_1_data: OrderDataDict) -> None:
    data = order_1.to_dict()
    expected_dict = order_1_data
    assert data == expected_dict

