from typing import override
import json
from abc import ABC

from src.model import ProductDataDict, CustomerDataDict, OrderDataDict

class FileReader[T]:
    """
    Abstract base class for reading data from files.

    This class provides a generic interface for reading data from files and 
    returning it as a list of objects of type `T`.

    Type Parameters:
        - T: The type of objects that the file reader will return.

    Methods:
        - read(file_name: str) -> list[T]:
            Reads data from a file and returns it as a list of objects of type `T`.

    Example Usage:
        To create a concrete file reader, subclass `FileReader` and specify the type `T`.
        For example:
        >>> class ProductJsonFileReader(FileReader[ProductDataDict]):
        ...     pass
    """

    def read(self, file_name: str) -> list[T]:
        """
        Read data from a file and return it as a list of objects.

        Args:
            file_name (str): The name of the file to read.

        Returns:
            list[T]: A list of objects of type `T` read from the file.

        Raises:
            FileNotFoundError: If the file does not exist.
            JSONDecodeError: If the file contains invalid JSON.
        """
        with open(file_name, 'r', encoding='utf-8') as file:
            return json.load(file)    
        
class ProductJsonFileReader(FileReader[ProductDataDict]):
    """
    A concrete implementation of `FileReader` for reading product data.

    This class reads JSON files containing product data and returns it as a list of `ProductDataDict` objects.
    """
    pass

class CustomerJsonFileReader(FileReader[CustomerDataDict]):
    """
    A concrete implementation of `FileReader` for reading customer data.

    This class reads JSON files containing customer data and returns it as a list of `CustomerDataDict` objects.
    """
    pass

class OrderJsonFileReader(FileReader[OrderDataDict]):
    """
    A concrete implementation of `FileReader` for reading order data.

    This class reads JSON files containing order data and returns it as a list of `OrderDataDict` objects.
    """
    pass

class FileWriter[T]:
    """
    Abstract base class for writing data to files.

    This class provides a generic interface for writing data to files as JSON.

    Type Parameters:
        - T: The type of objects that the file writer will write.

    Methods:
        - write(file_name: str, data: list[T]) -> None:
            Writes a list of objects of type `T` to a file in JSON format.

    Example Usage:
        To create a concrete file writer, subclass `FileWriter` and specify the type `T`.
        For example:
        >>> class ProductJsonFileWriter(FileWriter[ProductDataDict]):
        ...     pass
    """
    def write(self, file_name: str, data: list[T]) -> None:
        """
        Write data to a file in JSON format.

        Args:
            file_name (str): The name of the file to write to.
            data (list[T]): The list of objects to write to the file.

        Raises:
            IOError: If there is an error writing to the file.
        """
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

class ProductJsonFileWriter(FileWriter[ProductDataDict]):
    """
    A concrete implementation of `FileWriter` for writing product data.

    This class writes a list of `ProductDataDict` objects to a JSON file.
    """
    pass

class CustomerJsonFileWriter(FileWriter[CustomerDataDict]):
    """
    A concrete implementation of `FileWriter` for writing customer data.

    This class writes a list of `CustomerDataDict` objects to a JSON file.
    """
    pass    

class OrderJsonFileWriter(FileWriter[OrderDataDict]):
    """
    A concrete implementation of `FileWriter` for writing order data.

    This class writes a list of `OrderDataDict` objects to a JSON file.
    """
    pass