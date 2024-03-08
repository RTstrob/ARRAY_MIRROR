class Array:
    def to_linked_list(self, array: Array) -> LinkedList: 
        linked_list = []
        if not isinstance(array, Array):
            raise TypeError ("Input must be an Array.")
        
        for i in range(array._logical_size + 1):
            if i == 0:
                node = array._items[0]
                self._head = node
                node._previous = None
                node._next = array._items[1]
                linked_list.append(node)
            elif i > 0 and i < self._logical_size:
                node = array._items[i]
                node._previous = array._items[i - 1]
                node._next = array.items[i + 1]
                linked_list.append(node)
            elif i == self._logical_size:
                node = array._items[i]
                self._tail = node
                node._previous = array._items[i - 1]
                node._next = None
                linked_list.append(node)
        return linked_list

