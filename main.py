from src.file_service import (
    ProductJsonFileReader, 
    CustomerJsonFileReader, 
    OrderJsonFileReader,
    ProductJsonFileWriter,
    CustomerJsonFileWriter,
    OrderJsonFileWriter
)
from src.model import ProductCategory, ShippingMethod
from src.validator import Validator
from decimal import Decimal


def test_1() -> None:
    product_json_file_reader = ProductJsonFileReader()
    file_name = "./data/products.json"
    products = product_json_file_reader.read(file_name)
    for product in products:
        print(product)

    product_json_file_writer = ProductJsonFileWriter()
    file_name = "./data_out/products_out.json"
    product_json_file_writer.write(file_name, products)

    print('-' * 20) 
    customer_json_file_reader = CustomerJsonFileReader()
    file_name = "./data/customers.json"
    customers = customer_json_file_reader.read(file_name)
    for customer in customers:
        print(customer)
    
    casetomer_json_file_writer = CustomerJsonFileWriter()
    file_name = "./data_out/customers_out.json"
    casetomer_json_file_writer.write(file_name, customers)

    print('-' * 20) 
    order_json_file_reader = OrderJsonFileReader()      
    file_name = "./data/orders.json"
    orders = order_json_file_reader.read(file_name)
    for order in orders:
        print(order)
    
    order_json_file_writer = OrderJsonFileWriter()
    file_name = "./data_out/orders_out.json"    
    order_json_file_writer.write(file_name, orders)

def test_2_validator() -> None:
    print(Validator.is_valid_value_of("Standard", ProductCategory))
    print(Validator.is_valid_value_of("Electronics", ProductCategory))
    print(Validator.is_valid_value_of("Standard", ShippingMethod))
    print(Validator.is_valid_value_of("Express", ShippingMethod))
    print(Validator.is_valid_value_of("EXPREs", ShippingMethod))

def test_3_email() -> None:
    print(Validator.is_valid_email('jacek.hercog@gmail.com'))  
    print(Validator.is_valid_email('jacek.hercog@gcc'))
 
def test_4_validete_int_and_decimal_in_range() -> None:
    print(Validator.validate_int_in_range(1, 1, 10))
    print(Validator.validate_int_in_range(0, 1, 10))
    print(Validator.validate_int_in_range(11, 1, 10))
    print(Validator.validate_int_in_range(-1, -1, 10))
    print(Validator.validate_decimal_in_range('5.5', Decimal('1.0'), Decimal('10.0')))
    print(Validator.validate_decimal_in_range('abc', Decimal('1.0'), Decimal('10.0')))
    print(Validator.validate_decimal_in_range('5.5', Decimal('-1.0'), Decimal('10.0')))

def test_5_validate_string_with_regex() -> None:
    print(Validator.validate_string_with_regex('1234567890', r'^\d{10}$'))
    print(Validator.validate_string_with_regex('123456789', r'^\d{10}$'))
    print(Validator.validate_string_with_regex('ALA', r'[A-Z]+'))
    print(Validator.validate_string_with_regex('ALa', r'[A-Z]+'))

def main() -> None:
    # test_1()
    # test_2_validator()
    # test_3_email()
    # test_4_validete_int_and_decimal_in_range()
    test_5_validate_string_with_regex()
    
    

if __name__ == "__main__":  
    main()
    