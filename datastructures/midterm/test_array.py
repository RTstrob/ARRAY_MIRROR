import pytest
from midterm import array

class TestClassTemplate:
    def to_linked_list_with_not_array(self):
        test_array = "Test!"
        with pytest.raises(TypeError):
            test_array.to_linked_list()
