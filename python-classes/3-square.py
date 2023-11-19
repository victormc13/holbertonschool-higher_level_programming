#!/usr/bin/python3

"""Square class"""


class Square:
    """Class representing a square"""

    def __init__(self, size=0):
        """Initialize a new Square instance.

        Args:
            size (int, optional): size of the square. Defaults to 0.

        Raises:
            TypeError: If size if not an integer.
            ValueError: If size is less than 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        self.__size = size

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: area of the square.

        """
        return self.__size ** 2
