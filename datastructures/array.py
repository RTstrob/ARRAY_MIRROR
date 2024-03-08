# datastructures.array.Array

""" This module defines an Array class that represents a one-dimensional array. 
    The Array class is a dynamically growing array data structure. 
    The Array class uses a numpy array as the internal data structure. 
    The Array class adheres to the docstring requirements per method, including raising appropriate exceptions where indicated.
"""


from typing import Any
import numpy as np

class Array:
    """Array class - representing a one-dimensional array.
        Stipulations:
            1. Must use a numpy array as the internal data structure.
            2. Must adhere to the docstring requirements per method, including raising
               raising appropriate exceptions where indicated.
    """

    def __init__(self, size: int = 0, default_item_value: Any = None) -> None:
        """ Array Constructor. Initializes the Array with a default capacity and default value.

        Examples:
            >>> array_one = Array()
            >>> print(array_one)
            []
            >>> array_two = Array(size=10)
            >>> print(array_two)
            [None, None, None, None, None, None, None, None, None, None]
            >>> array_three = Array(size=10, default_item_value=0)
            >>> print(array_three)
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        Args:
            size (int): the desired capacity of the Array (default is 0)
            default_item_value (Any): the desired default value of the Array (default is None)

        Returns:
            None
        """
        self._items = np.array([default_item_value] * size, dtype=object)
        self._default_item_value = default_item_value
        self._logical_size = size
        self._physical_size = size

    @staticmethod
    def from_list(list_items: list) -> 'Array':
        """
        Create an Array from a Python list.
        
        Examples: 
            >>> array = Array.from_list([1, 2, 3])
            >>> print(array) 
            [1, 2, 3]
        
        Args:
            list_items (list): the list to create the Array from.
            
        Returns:
            array (Array): A new Array instance containing the items from `list_items`
        
        Raises:
            TypeError: if list_items is not a list.
        """
        #input must be a list
        if not isinstance(list_items, list):
            raise TypeError("Input must be a list")
        
        new_array = Array(size=len(list_items))
        for i, item in enumerate(list_items):
            new_array[i] = item
        
        return new_array
    
    def __getitem__(self, index: int) -> Any:
        """ Bracket operator for getting an item from an Array.

        Examples:
            >>> array = Array.from_list(['zero', 'one', 'two', 'three', 'four'])
            >>> print(array[0]) # invokes __getitem__ using the [] operator
            zero

        Args:
            index (int): the desired index.
        
        Returns:
            Any: the item at the index.
        
        Raises:
            IndexError: if the index is out of bounds.
        """
        if index < 0 or index >= len(self._items):
            raise IndexError('Must be in range of array.')
        
        return self._items[index]

    def __setitem__(self, index: int, data: Any) -> None:
        """ Bracket operator for setting an item in an Array.

        Examples:
            >>> array = Array.from_list(['zero', 'one', 'two', 'three', 'four'])
            >>> array[0] = 'new zero' # invokes __setitem__
            >>> print(array[0])
            new zero

        Args:
            index (int): the desired index to set.
            data (Any): the desired data to set at index.
        
        Returns:
            None
        
        Raises: 
            IndexError: if the index is out of bounds.
        """
        if index < 0 or index > self._logical_size - 1:
            raise IndexError(f'Index {index} out of bounds') 
        self._items[index] = data

    def append(self, data: Any) -> None:
        """ Append an item to the end of the Array

        Examples:
            >>> array = Array.from_list(['zero', 'one', 'two', 'three', 'four'])
            >>> array.append('five') # invokes append
            >>> print(array)
            [zero, one, two, three, four, five]

        Args:
            data (Any): the desired data to append.

        Returns:
            None
        """
        if self._physical_size == self._logical_size:
            new_size = 1 if self._physical_size == 0 else self._physical_size*2
            new_items = np.array([self._default_item_value] * new_size, dtype=object)

            self._physical_size = new_size
            for i in range(self._logical_size):
                new_items[i] = self._items[i]
            self._items = new_items

        self._items[self._logical_size] = data
        self._logical_size += 1
        
    def __len__(self) -> int:
        """ Length operator for getting the logical length of the Array (number of items in the Array).

        Examples:
            >>> array = Array.from_list(['zero', 'one', 'two', 'three', 'four'])
            >>> print(len(array))
            5

        Returns:
            length (int): the length of the Array.
        """
        return self._logical_size

    def resize(self, new_size: int, default_value: Any = None) -> None:
        """ Resize an Array. Resizing to a size smaller than the current size will truncate the Array. Resizing to a larger size will append None to the end of the Array.

        Examples:
            >>> array = Array.from_list(['zero', 'one', 'two', 'three', 'four'])
            >>> array.resize(3) 
            >>> print(array)
            [zero, one, two]
            >>> array.resize(5)
            >>> print(len(array))
            5
            >>> print(array)
            [zero, one, two, None, None]

        Args:
            new_size (int): the desired new size of the Array.
            default_value (Any): the desired default value to append to the Array if the new size is larger than the current size. Only makes sense if the new_size is larger than the current size. (default is None).
        
        Returns:
            None
        
        Raises:
            ValueError: if the new size is less than 0.
        """
        if new_size < 0:
            raise ValueError()
        
        copy_size = new_size if new_size < self._physical_size else self._physical_size
        new_items = np.array([self._default_item_value] * new_size, dtype=object)
        for i in range(copy_size):
            new_items[i] = self._items[i]
        self._items = new_items

        self._physical_size = self._logical_size = new_size

    def __eq__(self, other: object) -> bool:
        """ Equality operator == to check if two Arrays are equal (deep check).

        Examples:
            >>> array1 = Array.from_list(['zero', 'one', 'two', 'three', 'four'])
            >>> array2 = Array.from_list(['zero', 'one', 'two', 'three', 'four'])
            >>> print(array1 == array2) 
            True

        Args:
            other (object): the instance to compare self to.
        
        Returns:
            is_equal (bool): true if the arrays are equal (deep check).
        """
        if not isinstance(other, Array):
            raise TypeError("Input must be an array.")
        
        if len(self._items) != len(other._items):
            return False
        
        for i in range(self._logical_size):
            if self._items[i] != other._items[i]:
                return False
        return True


    def __ne__(self, other: object) -> bool:
        """ Non-Equality operator !=.
        
        Examples:
            >>> array1 = Array.from_list(['zero', 'one', 'two', 'three', 'four'])
            >>> array2 = Array.from_list(['zero', 'one', 'two', 'three', 'four'])
            >>> print(array1 != array2)
            False
        
        Args:
            other (object): the instance to compare self to.
            
        Returns:
            is_not_equal (bool): true if the arrays are NOT equal (deep check).
        """
        if not isinstance(other, Array):
            raise TypeError("Input must be an array.")
        
        if len(self._items) != len(other._items):
            return True
        
        for i in range(self._logical_size):
            if self._items[i] != other._items[i]:
                return True
        return False

    def __iter__(self) -> Any:
        """ Iterator operator. Allows for iteration over the Array.
        Examples:
            >>> array = Array.from_list(['zero', 'one', 'two', 'three', 'four'])
            >>> for item in array: print(item, end=' ') # invokes iter
            zero one two three four 

        Yields:
            item (Any): yields the item at index
        """
        for i in range(self._logical_size):
            yield self._items[i]

    def __reversed__(self) -> Any:
        """ Reversed iterator operator. Allows for iteration over the Array in reverse.
        Examples:

            >>> array = Array.from_list(['zero', 'one', 'two', 'three', 'four'])
            >>> for item in reversed(array): print(item, end= ' ') # invokes __reversed__
            four three two one zero 

        Yields:
            item (Any): yields the item at index starting at the end
        """
        for i in range(self._logical_size - 1, -1, -1):
            yield self._items[i]

    def __delitem__(self, index: int) -> None:
        """ Delete an item in the array. Copies the array contents from index + 1 down
            to fill the gap caused by deleting the item and shrinks the array size down by one.

        Examples:

            >>> array = Array.from_list(['zero', 'one', 'two', 'three', 'four'])
            >>> del array[2]
            >>> print(array)
            [zero, one, three, four]
            >>> len(array)
            4

        Args:
            index (int): the desired index to delete.
        
        Returns:
            None
        """
        if index < 0 or index >= self._logical_size:
            raise IndexError("Index out of range")
        
        new_items = np.array([self._default_item_value] * (self._logical_size - 1), dtype=object)
        
        for i in range(0, index):
            new_items[i] = self._items[i]

        for i in range(index, self._logical_size - 1):
            new_items[i] = self._items[i + 1]
        self._items = new_items

        self._logical_size -= 1
        self._physical_size = self._logical_size

    def __contains__(self, item: Any) -> bool:
        """ Contains operator (in). Checks if the array contains the item.

        Examples:

            >>> array = Array.from_list(['zero', 'one', 'two', 'three', 'four'])
            >>> print('three' in array)
            True

        Args:
            item (Any): the desired item to check whether it's in the array.

        Returns:
            contains_item (bool): true if the array contains the item.
        """
        for i in range(self._logical_size):
            if self._items[i] == item:
                return True
        return False
    
    def __does_not_contain__(self, item: Any) -> bool:
        """ Does not contain operator (not in)

        Examples:

            >>> array = Array.from_list(['zero', 'one', 'two', 'three', 'four'])
            >>> print('five' not in array)
             True

        Args:
            item (Any): the desired item to check whether it's in the array.

        Returns:
            does_not_contains_item (bool): true if the array does not contain the item.
        """ 
        for i in range(self._logical_size):
            if self._items[i] == item:
                return False
        return True

    def clear(self) -> None:
        """ Clear the Array
        
        Examples:
        
            >>> array = Array.from_list(['zero', 'one', 'two', 'three', 'four'])
            >>> array.clear()
            >>> print(array)
            []
            >>> print(len(array))
            0
            
        Returns:
            None
        """
        self._items = []
        self._physical_size = 0
        self._logical_size = 0 

    def __str__(self) -> str:
        """ Return a string representation of the data and structure. 

        Examples:

            >>> array = Array.from_list(['zero', 'one', 'two', 'three', 'four'])
            >>> print(array)
            [zero, one, two, three, four]

        Returns:
            string (str): the string representation of the data and structure.
        """
        return str(self._items[:self._logical_size])
    
    def __repr__(self) -> str:
        """ Return a string representation of the data and structure.
        
        Examples:
    
            >>> array = Array.from_list(['zero', 'one', 'two', 'three', 'four'])
            >>> print(repr(array))
        [zero, one, two, three, four]
        
        Returns:
            string (str): the string representation of the data and structure.
        """
        return self.__str__()

