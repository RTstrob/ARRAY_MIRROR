# This is a file you can copy/paste to create a new test file.
# Just make sure the new name starts with test_ and ends with .py.

# import data structures like this:
# from datastructures.array import Array

from datastructures.linked_list import LinkedList
import PyTest

class TestClassTemplate:
    def test_insert_after_should_insert_2_after_3(self):
        # Arrange (set up your test data)
        linked_list = LinkedList()
        expected = 0

        for i in range(5):
            if i == 3:
                continue
            linked_list.append(i)
        # Act (perform the action you want to test)
        linked_list.insert_after(2, 3)

        # Assert (check that the test is passing)
        assert 'something' == 'something'
