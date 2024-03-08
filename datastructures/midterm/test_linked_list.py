import pytest
from midterm import linked_list

class TestClassTemplate:
    def to_array_with_not_linked_list(self):
        test_linked_list = "Test!"
        with pytest.raises(TypeError):
            test_linked_list.to_array()
