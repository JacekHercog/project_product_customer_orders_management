from src.model import (
    Product,
    Customer,
    Order,
    ProductDataDict,
    CustomerDataDict,
    OrderDataDict
)

def test_product_to_dict(product_1: Product, product_1_data: ProductDataDict) -> None:
    """
    Test the `to_dict` method of the Product class.

    Args:
        product_1 (Product): A Product instance to be tested.
        product_1_data (ProductDataDict): The expected dictionary representation of the product.

    Asserts:
        The dictionary returned by `to_dict` matches the expected dictionary.
    """
    data = product_1.to_dict()
    excepted_dict = product_1_data
    assert data == excepted_dict

def test_customer_to_dict(customer_1: Customer, customer_1_data: CustomerDataDict) -> None:
    """
    Test the `to_dict` method of the Customer class.

    Args:
        customer_1 (Customer): A Customer instance to be tested.
        customer_1_data (CustomerDataDict): The expected dictionary representation of the customer.

    Asserts:
        The dictionary returned by `to_dict` matches the expected dictionary.
    """
    data = customer_1.to_dict()
    excepted_dict = customer_1_data
    assert data == excepted_dict

def test_order_to_dict(order_1: Order, order_1_data: OrderDataDict) -> None:
    """
    Test the `to_dict` method of the Order class.

    Args:
        order_1 (Order): An Order instance to be tested.
        order_1_data (OrderDataDict): The expected dictionary representation of the order.

    Asserts:
        The dictionary returned by `to_dict` matches the expected dictionary.
    """
    data = order_1.to_dict()
    expected_dict = order_1_data
    assert data == expected_dict

