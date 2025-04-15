from src.file_service import (
    ProductJsonFileReader, 
    CustomerJsonFileReader, 
    OrderJsonFileReader,
    ProductJsonFileWriter,
    CustomerJsonFileWriter,
    OrderJsonFileWriter
)

def main() -> None:
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


if __name__ == "__main__":  
    main()
    