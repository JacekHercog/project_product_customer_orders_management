from abc import ABC, abstractmethod     
from dataclasses import dataclass               
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

class Validator[T](ABC):
    """
    Abstract base class for validators.
    """

    @abstractmethod
    def validate(self, data: T) -> bool:
        """
        Validate the data.
        """
        pass

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
    
class ProductDataDictValidator(Validator[ProductDataDict]):
    """
    Validator for product data.
    """
    @override
    def validate(self, data: ProductDataDict) -> bool:
        """
        Validate the product data.
        """
        # Implement validation logic here
        return Validator.is_positive(data["price"])

@dataclass
class CustomerDataDictValidator(Validator[CustomerDataDict]):
    """
    Validator for customer data.
    """
    min_value: int = 0
    max_value: int = 65

    @override
    def validate(self, data: CustomerDataDict) -> bool:
        """
        Validate the customer data.
        """
        # Implement validation logic here
        return (
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

    @override
    def validate(self, data: OrderDataDict) -> bool:
        """
        Validate the order data.
        """
        # Implement validation logic here
        return (
            Validator.validate_decimal_in_range(str(data["discount"]), self.min_discount, self.max_discount)
            # and Validator.is_valid_value_of(data["shipping_method"], ShippingMethod)
        )