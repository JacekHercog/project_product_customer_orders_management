
from src.model import Product, ProductDataDict
from src.validator import ProductDataDictValidator
from src.converter import ProductConverter
from src.repository import ProductDataRepository
from src.file_service import ProductJsonFileReader
from pathlib import Path
import json

"""
Integration test
"""
def test_product_data_repository_with_real_json_file(
        tmp_path: Path,
        product_1: Product,
        product_2: Product,
        product_1_data: ProductDataDict,
        product_2_data: ProductDataDict) -> None:

    file_name = "tmp_products.json"
    test_file = tmp_path / file_name

    sample_data = [product_1_data, product_2_data]

    with open(test_file, 'w') as file:
        json.dump(sample_data, file)

    product_json_file_reader = ProductJsonFileReader()
    validator = ProductDataDictValidator()
    converter = ProductConverter()

    product_data_repository = ProductDataRepository(
        file_reader=product_json_file_reader,
        validator=validator,
        converter=converter,
        file_name=str(test_file)
    )

    data = product_data_repository.get_data()

    assert len(data) == 2
    assert data[0] == product_1
    assert data[1] == product_2
