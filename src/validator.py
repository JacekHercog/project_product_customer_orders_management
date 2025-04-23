from dataclasses import dataclass, field           
from decimal import Decimal, InvalidOperation
from enum import Enum
from typing import Type, override
from email_validator import validate_email, EmailNotValidError
import re
import logging
from src.model import (
    ProductDataDict, 
    CustomerDataDict, 
    OrderDataDict,
    ProductCategory,
    ShippingMethod)

logging.basicConfig(level=logging.INFO)

@dataclass
class Validator[T]:
    """
    Abstract base class for validators.
    """
    required_fields: list[str] = field(default_factory=list)
                                       
    def validate(self, data: T) -> bool:
        """
        Validate the data.
        """
        return len(self.required_fields) == 0 or self.has_required_keys(data, self.required_fields)

    def has_required_keys(self, data: T, keys: list[str]) -> bool:
        """
        Check if the data has the required fields.
        """
        missing_keys = []
        for key in keys:
            if isinstance(data, dict):
                if key not in data:
                    missing_keys.append(key)
            elif not hasattr(data, key):
                missing_keys.append(key)        
        if missing_keys:
            logging.error(f"Missing keys: {', '.join(missing_keys)}")
            return False            
        return True
    

    @staticmethod
    def is_positive(data: int | str) -> bool:
        """
        Check if the data is positive.
        """
        match data:
            case int(value) if value > 0:
                return True                
            case str(value):
                try:
                    decimal_value = Decimal(value)
                    return decimal_value > 0
                except InvalidOperation as e:
                    logging.error(f"{str(e)}")
                    return False
            case _:
                return False
    
    @staticmethod
    def is_valid_value_of(value: str, enum_class: Type[Enum]) -> bool:
        """
        Check if the value is a valid value of the enum.
        """
        return value in [item.value for item in enum_class]
    
    @staticmethod
    def is_valid_email(email: str) -> bool:
        """
        Validate the email address.
        """
        try:
            validate_email(email, check_deliverability=True)
            return True
        except EmailNotValidError as e:
            logging.error(f"{str(e)}")
            return False   

    @staticmethod
    def validate_int_in_range(value: int, min_value: int, max_value: int) -> bool:
        """
        Check if the integer value is in the specified range.
        """
        return min_value <= value <= max_value 

    @staticmethod
    def validate_decimal_in_range(value: str, min_value: Decimal, max_value: Decimal) -> bool:
        """
        Check if the decimal value is in the specified range.
        """
        try:
            decimal_value = Decimal(value)
            return min_value <= decimal_value <= max_value
        except InvalidOperation as e:
            logging.error(f"{str(e)}")
            return False
        
    @staticmethod
    def validate_string_with_regex(value: str, pattern: str) -> bool:
        """
        Validate the string with the given regex.
        """
        return re.fullmatch(pattern, value) is not None
        # if re.match(regex, value):
        #     return True
        # else:
        #     logging.error(f"String '{value}' does not match the regex '{regex}'")
        #     return False

@dataclass    
class ProductDataDictValidator(Validator[ProductDataDict]):
    """
    Validator for product data.
    """

    def __post_init__(self) -> None:
        """
        Initialize the validator.
        """
        if len(self.required_fields) == 0:
            self.required_fields = ["id", "name", "category", "price"]

    @override
    def validate(self, data: ProductDataDict) -> bool:
        """
        Validate the product data.
        """
        return super().validate(data) and Validator.is_positive(data["price"])


@dataclass
class CustomerDataDictValidator(Validator[CustomerDataDict]):
    """
    Validator for customer data.
    """
    min_value: int = 0
    max_value: int = 65
    
    def __post_init__(self) -> None:
        """
        Initialize the validator.
        """
        if len(self.required_fields) == 0:
            self.required_fields = ["id", "first_name", "last_name", "age", "email"]

    @override
    def validate(self, data: CustomerDataDict) -> bool:
        """
        Validate the customer data.
        """
        return super().validate(data) and (
            Validator.validate_int_in_range(int(data["age"]), self.min_value, self.max_value)  
            # and Validator.is_valid_email(data["email"])
        )
    
@dataclass
class OrderDataDictValidator(Validator[OrderDataDict]):
    """
    Validator for order data.
    """
    min_discount: Decimal = Decimal('0.0')
    max_discount: Decimal = Decimal('1.0')
    
    def __post_init__(self) -> None:
        """
        Initialize the validator.
        """
        if len(self.required_fields) == 0:
            self.required_fields = ["id", "customer_id", "product_id", "quantity", "discount", "shipping_method"]

    @override
    def validate(self, data: OrderDataDict) -> bool:
        """
        Validate the order data.
        """
        return super().validate(data) and (
            Validator.validate_decimal_in_range(str(data["discount"]), self.min_discount, self.max_discount)
            # and Validator.is_valid_value_of(data["shipping_method"], ShippingMethod)
        )