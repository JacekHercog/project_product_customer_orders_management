from src.model import Product, ProductDataDict
from src.validator import ProductDataDictValidator
from src.converter import ProductConverter
from src.repository import ProductDataRepository
from src.file_service import ProductJsonFileReader
from pathlib import Path
import json

"""
Integration test for the ProductDataRepository with a real JSON file.
"""

def test_product_data_repository_with_real_json_file(
        tmp_path: Path,
        product_1: Product,
        product_2: Product,
        product_1_data: ProductDataDict,
        product_2_data: ProductDataDict) -> None:
    """
    Test the integration of ProductDataRepository with a real JSON file.

    Args:
        tmp_path (Path): A temporary directory provided by pytest for creating test files.
        product_1 (Product): The first product instance to be tested.
        product_2 (Product): The second product instance to be tested.
        product_1_data (ProductDataDict): The dictionary representation of the first product.
        product_2_data (ProductDataDict): The dictionary representation of the second product.

    Steps:
        1. Create a temporary JSON file with sample product data.
        2. Initialize the ProductDataRepository with the real JSON file.
        3. Retrieve data from the repository.
        4. Assert that the retrieved data matches the expected product instances.

    Asserts:
        - The number of products retrieved matches the number of products in the JSON file.
        - The retrieved products match the expected product instances.
    """
    file_name = "tmp_products.json"
    test_file = tmp_path / file_name

    # Write sample data to the temporary JSON file
    sample_data = [product_1_data, product_2_data]
    with open(test_file, 'w') as file:
        json.dump(sample_data, file)

    # Initialize the repository with the real JSON file
    product_json_file_reader = ProductJsonFileReader()
    validator = ProductDataDictValidator()
    converter = ProductConverter()

    product_data_repository = ProductDataRepository(
        file_reader=product_json_file_reader,
        validator=validator,
        converter=converter,
        file_name=str(test_file)
    )

    # Retrieve data from the repository
    data = product_data_repository.get_data()

    # Assertions
    assert len(data) == 2
    assert data[0] == product_1
    assert data[1] == product_2
