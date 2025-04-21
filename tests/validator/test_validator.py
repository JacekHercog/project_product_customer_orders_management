import pytest
from src.validator import (
    Validator, ProductDataDictValidator, CustomerDataDictValidator, OrderDataDictValidator
)
from src.model import (
    ProductCategory, ShippingMethod, ProductDataDict, CustomerDataDict, OrderDataDict
)
from decimal import Decimal
from enum import Enum
from email_validator import EmailNotValidError

@pytest.mark.parametrize(
    "value, expected",
    [
        (1, True),
        (0, False),
        (-1, False),
        ("1", True),
        ("0", False),
        ("-1", False),
        ("1.0", True),
        ("0.0", False),
        ("-1.0", False),
        ("abc", False),
        ("123abc", False),
    ]
)
def test_is_positive(value: int, expected: bool) -> None:
    assert Validator.is_positive(value) == expected

@pytest.mark.parametrize("value, enum_class, expected", [
    ("Standard", ProductCategory, False),
    ("Electronics", ProductCategory, True),
    ("Standard", ShippingMethod, True),
    ("Express", ShippingMethod, True),
    ("EXPREs", ShippingMethod, False),
])
def test_is_valid_value_of(value: str, enum_class: type[Enum], expected: bool) -> None:
    assert Validator.is_valid_value_of(value, enum_class) == expected
    
@pytest.mark.parametrize("email, expected", 
                         [
                            ("jacek.hercog@gmail.com", True),
                            ("jacek.hercog@gcc", False),
                            ("jacek.hercog@gmail", False),
                            # ("jacek.hercog@.com", False),
                            # ("jacek.hercog@com", False),
                            # ("jacek.hercog@com.", False),
                            # ("jacek.hercog@gmail..com", False),
                            ("jacek.hercog@gwp.pl", True)

                         ])
def test_is_valid_email(email: str, expected: bool) -> None:
    assert Validator.is_valid_email(email) == expected

@pytest.mark.parametrize("value, min_value, max_value, expected", [
    (1, 1, 10, True),
    (0, 1, 10, False),
    (11, 1, 10, False),
    (-1, -1, 10, True)
    
])
def test_validate_int_in_range(value: int, min_value: int, max_value: int, expected: bool) -> None:
    assert Validator.validate_int_in_range(value, min_value, max_value) == expected


@pytest.mark.parametrize("value, min_value, max_value, expected", [
    ("5.5", Decimal("1.0"), Decimal("10.0"), True),
    ("abc", Decimal("1.0"), Decimal("10.0"), False),
    ("-5.5", Decimal("-10.0"), Decimal("-1.0"), True),
    ("-11.5", Decimal("-10.0"), Decimal("-1.0"), False),
    ("11.5", Decimal("1.0"), Decimal("10.0"), False)
])
def test_validate_decimal_in_range(value: str, min_value: Decimal, 
                                   max_value: Decimal, expected: bool) -> None:
    assert Validator.validate_decimal_in_range(value, min_value, max_value) == expected

@pytest.mark.parametrize("value, pattern, expected", [
    ("abc123", r"^[a-zA-Z0-9]+$", True),
    ("abc 123", r"^[a-zA-Z0-9]+$", False),
    ("abc_123", r"^[a-zA-Z0-9]+$", False),
    ("abc@123", r"^[a-zA-Z0-9]+$", False),
    ("ABC", r'[A-Z]+', True)
])
def test_validate_string_with_regex(value: str, pattern: str, expected: bool) -> None:
    assert Validator.validate_string_with_regex(value, pattern) == expected


# @pytest.mark.parametrize("data, expected", [
#     ({"id": 1, "name": "Laptop", "category": "Electronics", "price": "121.12"}, True),
#     ({"id": 2, "name": "Laptop", "category": "Electronics", "price": "0.0"}, False)
# ])
@pytest.mark.parametrize("data, expected", [
    ({"price": "121.12"}, True),
    ({"price": "-1.0"}, False),
    ({"price": "0"}, False),
    ({"price": "abc"}, False)
])
def test_ProductDataDictValidator(data:ProductDataDict, expected: bool) -> None:
    validator = ProductDataDictValidator()
    assert validator.validate(data) == expected
 

@pytest.mark.parametrize("data, min_age, max_age, expected", [
    ({"age": 20}, 18, 65, True),
    ({"age": 86}, 18, 86, True),
    ({"age": 86}, 18, 65, False)
])
def test_CustomerDataDictValidator(data: CustomerDataDict, min_age: int, max_age: int, expected: bool  ) -> None:
    validator = CustomerDataDictValidator(min_age, max_age)  
    assert validator.validate(data) == expected

@pytest.mark.parametrize("data, expected", [
    ({"id": 1, "product_id": 1, "customer_id": 1, "discount": "0.5"}, True),
    ({"id": 2, "product_id": 2, "customer_id": 2, "discount": "-0.5"}, False),
    ({"id": 3, "product_id": 2, "customer_id": 2, "discount": "0.0"}, True),
    ({"id": 4, "product_id": 2, "customer_id": 2, "discount": "1.0"}, True),
    ({"id": 5, "product_id": 2, "customer_id": 2, "discount": "abc"}, False)
])
def test_OrderDataDictValidator(data: OrderDataDict, expected: bool) -> None:
    validator = OrderDataDictValidator()
    assert validator.validate(data) == expected
    