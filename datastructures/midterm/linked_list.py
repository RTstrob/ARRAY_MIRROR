class LinkedList:
    def to_array(self) -> Array:
        array = []
        current_node = self._head
        if not isinstance(LinkedList):
            raise TypeError("Input must be a linked list.")
        for i in range(self._logical_size):
            array.append(current_node)
            current_node = current_node._next
        return array
