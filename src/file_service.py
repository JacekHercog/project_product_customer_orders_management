from typing import override
import json
from abc import ABC

from src.model import ProductDataDict, CustomerDataDict, OrderDataDict

class AbstractFileReader[T](ABC):
    """
    Abstract base class for FileReader.
    """

    def read(self, file_name: str) -> list[T]:
        """
        Read data from a file and return it as a list of objects.
        """
        with open(file_name, 'r', encoding='utf-8') as file:
            return json.load(file)    
        
class ProductJsonFileReader(AbstractFileReader[ProductDataDict]):
    pass

class CustomerJsonFileReader(AbstractFileReader[CustomerDataDict]):
    pass

class OrderJsonFileReader(AbstractFileReader[OrderDataDict]):
   pass

class AbstractFileWriter[T](ABC):
    """
    Abstract base class for FileWriter.
    """
    def write(self, file_name: str, data: list[T]) -> None:
        """
        Write data to a file.
        """
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

class ProductJsonFileWriter(AbstractFileWriter[ProductDataDict]):
    pass

class CustomerJsonFileWriter(AbstractFileWriter[CustomerDataDict]):
    pass    

class OrderJsonFileWriter(AbstractFileWriter[OrderDataDict]):
    pass