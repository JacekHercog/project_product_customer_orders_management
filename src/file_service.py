from typing import override
import json

from src.model import ProductDataDict, CustomerDataDict, OrderDataDict

class FileReader[T]:

    def read(self, file_name: str) -> list[T]:
        """
        Read data from a file and return it as a list of objects.
        """
        with open(file_name, 'r', encoding='utf-8') as file:
            return json.load(file)    
        
class ProductJsonFileReader(FileReader[ProductDataDict]):
    pass

class CustomerJsonFileReader(FileReader[CustomerDataDict]):
    pass

class OrderJsonFileReader(FileReader[OrderDataDict]):
   pass

class FileWriter[T]:
    def write(self, file_name: str, data: list[T]) -> None:
        """
        Write data to a file.
        """
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)

class ProductJsonFileWriter(FileWriter[ProductDataDict]):
    pass

class CustomerJsonFileWriter(FileWriter[CustomerDataDict]):
    pass    

class OrderJsonFileWriter(FileWriter[OrderDataDict]):
    pass