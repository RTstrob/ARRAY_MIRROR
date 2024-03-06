from __future__ import annotations
from typing import Any

from datastructures.list_node import ListNode


class LinkedList:
    """ Class LinkedList - representing an unordered linked list
        Depends on ListNode class to store the data, previous, and next nodes.
            Stipulations:
            1. Must manage the linked list using two ListNode objects (_head and _tail)
            2. Must adhere to the docstring requirements per method, including raising
               raising appropriate exceptions where indicated.
    """

    def __init__(self) -> None:
        """ Constructor for the LinkedList constructs an empty linked list.

        Examples:
            >>> linked_list = LinkedList()
            >>> print(linked_list)
            []
        
        Returns:
            None
        
        """
        raise NotImplementedError('LinkedList.__init__')

    @staticmethod
    def from_list(py_list: list) -> LinkedList:
        """ Create a new LinkedList from a Python list.

        Examples:
            >>> linked_list = LinkedList.from_list(['cat', 'dog', 'bird'])
            >>> print(linked_list)
            ['cat', 'dog', 'bird']
        
        Args:
            py_list (list): list to convert to a linked list.

        Returns:
            A new LinkedList instance.
        
        Raises:
            TypeError: if py_list is not a list.
        """
        raise NotImplementedError('LinkedList.from_list')

    def append(self, item: Any) -> None:
        """ Append an item to the end of the list.

        Examples:
            >>> linked_list = LinkedList()
            >>> linked_list.append('cat')
            >>> linked_list.append('dog')
            >>> print(linked_list)
            ['cat', 'dog']
        
        Args:
            item: the desired data to append to the linked list.
        
        Returns:
            None
        """
        if self._head is None:
            new_node = ListNode(item)
            self._head = self._tail = new_node

        else: #if the list has at least one node
            new_node = ListNode(item, self._tail)
            self._tail.next = new_node
            self._tail = new_node


    def prepend(self, item: Any) -> None:
        """ Prepend an item to the beginning of the list.
        
        Examples:
            >>> linked_list = LinkedList()
            >>> linked_list.prepend('cat')
            >>> linked_list.prepend('dog')
            >>> print(linked_list)
            ['dog', 'cat']
        
        Args:
            item (Any): the desired data to prepend to the linked list.
            
        Returns:
            None
        
        """
        raise NotImplementedError('LinkedList.prepend')

    def insert_before(self, before_item: Any, new_item: Any) -> None:
        """ Insert a new item before a specified item.
        
        Examples:
            >>> linked_list = LinkedList.from_list(['cat', 'dog', 'bird'])
            >>> linked_list.insert_before('dog', 'fish')
            >>> print(linked_list)
            ['cat', 'fish', 'dog', 'bird']
                
        Args:
            before_item (Any): the item that the user wishes to insert before.
            new_item (Any): the desired item to insert.
        
        Returns:
            None
        
        Raises:
            KeyError: if before_item is not found.
        """
        raise NotImplementedError('LinkedList.insert_before')

    def insert_after(self, after_item: Any, new_item: Any) -> None:
        """ Insert a new item after a specified item.

        Examples:
            >>> linked_list = LinkedList.from_list(['cat', 'dog', 'bird'])
            >>> linked_list.insert_after('dog', 'fish')
            >>> print(linked_list)
            ['cat', 'dog', 'fish', 'bird']

        Args:
            after_item (Any): the item that the user wishes to insert after.
            new_item (Any): the desired item to insert.

        Returns:
            None

        Raises:
            KeyError: if after_item is not found.
        
        """
        travel = self.head

        while travel is not None and travel.item != after_item:
            travel = travel.next

        if travel is None:
            raise IndexError(f'Did not find the node with value {after_item}')
        
        if travel is self.tail:
            self.append(new_item)

        else:
            new_node = ListNode(new_item, travel, travel.next)
            travel.next = new_node

            if new_node.next is not None:
                new_node.next.previous = new_node

            self._count += 1



    @property
    def head(self) -> ListNode | None:
        """ Return the ListNode instance pointing at the head of the linked list.
            Note: this method should be used for debug and test purposes only.
            
        Examples
            >>> linked_list = LinkedList.from_list(['cat', 'dog', 'bird'])
            >>> head = linked_list.head
            >>> print(head.item)
            cat
        
        Returns:
            head (ListNode | None): the ListNode instance representing the head of the linked list.
            
        """
        raise NotImplementedError('LinkedList.head')

    @property
    def tail(self) -> ListNode | None:
        """ Return the ListNode instance pointing at the tail of the linked list.
            Note: this method should be used for debug and test purposes only.
        
        Examples:
            >>> linked_list = LinkedList.from_list(['cat', 'dog', 'bird'])
            >>> tail = linked_list.tail
            >>> print(tail.item)
            bird
        
        Returns:
            tail (ListNode | None): the ListNode instance representing the tail of the linked list.
        """
        raise NotImplementedError('LinkedList.tail')

    @property
    def front(self) -> Any:
        """ Return the item at the front of the linked list.
        
        Examples:
            >>> linked_list = LinkedList.from_list(['cat', 'dog', 'bird'])
            >>> first_item = linked_list.front
            >>> print(first_item)
            cat
        
        Returns:
            front (Any): the item stored in the head of the list
            
        Raises:
            IndexError: if the list is empty.
        
        """
        raise NotImplementedError('LinkedList.front')

    @property
    def back(self) -> Any:
        """ Return the item at the back of the linked list.

        Examples:
            >>> linked_list = LinkedList.from_list(['cat', 'dog', 'bird'])
            >>> last_item = linked_list.back
            >>> print(last_item)    
            bird

        Returns:
            last (Any): the item stored in the tail of the list.
        
        Raises:
            IndexError: if the list is empty.
        """
        return self._tail.item

    def clear(self) -> None:
        """ Clear the linked list.

        Examples:
            >>> linked_list = LinkedList.from_list(['cat', 'dog', 'bird'])
            >>> linked_list.clear()
            >>> print(linked_list)
            []
        
        Returns:
            None
        """
        raise NotImplementedError('LinkedList.clear')

    def extract(self, item: Any) -> None:
        """ Extract an item from the Linked List.

        Examples:
            >>> linked_list = LinkedList.from_list(['cat', 'dog', 'bird'])
            >>> linked_list.extract('dog')
            >>> print(linked_list)
            ['cat', 'bird']

        Args:
            item (Any): the item to remove from the linked list.

        Returns:
            None

        Raises:
            KeyError: if the item is not found.
        """
        raise NotImplementedError('LinkedList.extract')

    @property
    def empty(self) -> bool:
        """ Property to determine whether the list is empty.
        
        Examples:
            >>> linked_list = LinkedList()
            >>> print(linked_list.empty)
            True
        
        Returns:
            bool: whether the list is empty.
        """
        return self._head is None

    def pop_front(self) -> None:
        """ Remove the first item in the linked list.
        
        Examples:
            >>> linked_list = LinkedList.from_list(['cat', 'dog', 'bird'])
            >>> linked_list.pop_front()
            >>> print(linked_list)
            ['dog', 'bird']
        
        Returns:
            None
        
        Raises:
            IndexError: if the list is empty.
            
        """
        raise NotImplementedError('LinkedList.pop_front')

    def pop_back(self) -> None:
        """ Remove the last item in the linked list.

        Examples:
            >>> linked_list = LinkedList.from_list(['cat', 'dog', 'bird'])
            >>> linked_list.pop_back()
            >>> print(linked_list)
            ['cat', 'dog']

        Returns:
            None
        
        Raises:
            IndexError: if the list is empty.
        """
        raise NotImplementedError('LinkedList.pop_back')

    def __contains__(self, item: Any) -> bool:
        """ Membership operator in.
        
        Examples:
            >>> linked_list = LinkedList.from_list(['cat', 'dog', 'bird'])
            >>> print('dog' in linked_list)
            True
        
        Args:
            item (Any): the item to search for.
            
        Returns:
            bool: whether the linked list contains the item.
        """
        raise NotImplementedError('LinkedList.__contains__')

    def __eq__(self, other: object) -> bool:
        """ Equality operator ==.
        
        Examples:
            >>> linked_list1 = LinkedList.from_list(['cat', 'dog', 'bird'])
            >>> linked_list2 = LinkedList.from_list(['cat', 'dog', 'bird'])
            >>> print(linked_list1 == linked_list2)
            True
        
        Args:
            other (object): the instance to compare self to.
            
        Returns:
            bool: whether the lists are equal (deep check).
        """
        raise NotImplementedError('LinkedList.__eq__')

    def __ne__(self, other: object) -> bool:
        """ Non-Equality operator !=.
        
        Examples:
            >>> linked_list1 = LinkedList.from_list(['cat', 'dog', 'bird'])
            >>> linked_list2 = LinkedList.from_list(['cat', 'dog', 'bird'])
            >>> print(linked_list1 != linked_list2)
            False
        
        Args:
            other (object): the instance to compare self to.
            
        Returns:
            bool: whether the lists are not equal (deep check).
        """
        raise NotImplementedError('LinkedList.__ne__')
    
    def __iter__(self) -> Any:
        """ Iterator operator.
        
        Examples:
            >>> linked_list = LinkedList.from_list(['cat', 'dog', 'bird'])
            >>> for item in linked_list:
            ...     print(item)
            cat
            dog
            bird
        
        Returns:
            Any: yields the item at ListNode.
        """
        raise NotImplementedError('LinkedList.__iter__')

    def __reversed__(self) -> Any:
        """ Reversed iterator operator.
        
        Examples:
            >>> linked_list = LinkedList.from_list(['cat', 'dog', 'bird'])
            >>> for item in reversed(linked_list):
            ...     print(item)
            bird
            dog
            cat
        
        Returns:
            Any: yields the item at ListNode.
        """
        raise NotImplementedError('LinkedList.__reversed__')

    def __len__(self) -> int:
        """ len operator for getting length of the linked list.
        
        Examples:
            >>> linked_list = LinkedList.from_list(['cat', 'dog', 'bird'])
            >>> size = len(linked_list)
            >>> print(size)
            3
        
        Returns:
            int: the length of the LinkedList.
        """
        raise NotImplementedError('LinkedList.__len__')

    def __str__(self) -> str:
        """ Return a string representation of the data and structure.
        
        Examples:
            >>> linked_list = LinkedList.from_list(['cat', 'dog', 'bird'])
            >>> print(linked_list)
            ['cat', 'dog', 'bird']
            
        Returns:
            str: the string representation of the data and structure.
            
        """
        raise NotImplementedError('LinkedList.__str__')
    
    def __repr__(self) -> str:
        """ Return a string representation of the data and structure.
        
        Examples:
            >>> linked_list = LinkedList.from_list(['cat', 'dog', 'bird'])
            >>> print(linked_list)
            ['cat', 'dog', 'bird']
            
        Returns:
            str: the string representation of the data and structure.
        
        """
        raise NotImplementedError('LinkedList.__repr__')