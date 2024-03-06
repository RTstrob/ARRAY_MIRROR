# This is a file you can copy/paste to create a new test file.
# Just make sure the new name starts with test_ and ends with .py.

# import data structures like this:
from datastructures.array import Array
import pytest


class TestClassTemplate:
    #testing the init function
    def test_init_length(self):
        test_array = Array(10)
        size = len(test_array)
        assert size == 10

    def test_init_size_0(self):
        test_array = Array(0)
        size = len(test_array)
        assert size == 0

    #testing from_list
    def test_from_list_works_right(self):
        test_array = Array(3)
        test_array_from_list = Array.from_list([None, None, None])
        assert test_array == test_array_from_list

    def test_from_list_with_not_list(self):
        with pytest.raises(TypeError):
            test_array = Array.from_list("3")


    #testing get_item
    def test_get_operator_should_get_values(self):
        # Arrange 
        test_array = Array(10)
        for i in range(10):
            test_array[i] = i
 
        # Act and Assert
        for i in range(10):
            assert test_array[i] == i

    def test_get_for_invalid_index(self):
        test_array = Array(5)
        with pytest.raises(IndexError):
            assert test_array[6] == None	

    #testing set_item
    def test_set_operator_should_set_values(self):
        # Arrange
        test_array = Array(10)
 
        # Act
        for i in range(10):
            test_array[i] = i
 
        # Assert
        for i in range(10):
            assert test_array[i] == i

    def test_set_size_0(self):
        test_array = Array(0)
        with pytest.raises(IndexError):
            test_array[0] = "TEST"
 
    def test_set_operator_should_raise_index_error_for_negative_value(self):
        # Arrange
        test_array = Array(10)
        
        # Act & Assert
        with pytest.raises(IndexError):
            test_array[-1]
            
    def test_set_operator_should_raise_index_error_for_out_of_bounds(self):
        # Arrange
        test_array = Array(10)
        
        # Act & Assert
        with pytest.raises(IndexError):
            test_array[11]

    #testing append
    def test_array_append_grows_by_one(self):
        test_array = Array(10,5)
        test_array.append(6)
        assert len(test_array) == 11

    def test_array_append_with_empty_values(self):
        test_array = Array(10)
        test_array.append(6)
        assert len(test_array) == 11

    def test_array_append_with_size_0(self):
        test_array = Array(0)
        test_array.append("TEST!")
        assert len(test_array) == 1

    #testing len
    def test_len_returns_right_answer(self):
        test_array = Array(5)
        assert len(test_array) == 5    

    #testing resize
    def test_array_resize_smaller_truncates(self):
        test_array = Array(10)
        test_array.resize(3)
        assert len(test_array) == 3

    def test_array_resize_bigger_fills_with_empty_values(self):
        #Arrange
        test_array = Array(size=5, default_item_value=0)

        #Act
        test_array.resize(new_size=10, default_value=0)
        
        #Assert
        for i in range(10):
            assert test_array[i] == 0
    
    def test_array_resize_negative_index(self):
        test_array = Array(5)
        with pytest.raises(ValueError):
            test_array.resize(-5)

    #testing eq
    def test_eq_input_not_array(self):
        test_array = Array(5)
        other_array = "TEST"
        with pytest.raises(TypeError):
            test_array == other_array

    def test_eq_input_same_values(self):
        test_array = Array(5)
        other_array = Array(5)
        assert test_array == other_array

    def test_eq_inputs_different_lengths(self):
        test_array = Array(5)
        other_array = Array(10)
        with pytest.raises(AssertionError):
            assert test_array == other_array

    def test_eq_input_different_values(self):
        test_array = Array(5)
        other_array = Array(5, "TEST")
        with pytest.raises(AssertionError):
            assert test_array == other_array

    #testing ne
    def test_ne_input_not_array(self):
        test_array = Array(5)
        other_array = "TEST"
        with pytest.raises(TypeError):
            test_array == other_array
    
    def test_ne_input_same_values(self):
        test_array = Array(5)
        other_array = Array(5)
        with pytest.raises(AssertionError):
            assert test_array != other_array

    def test_ne_inputs_different_lengths(self):
        test_array = Array(5)
        other_array = Array(10)
        assert test_array != other_array

    def test_ne_input_different_values(self):
        test_array = Array(5)
        other_array = Array(5, "TEST")
        assert test_array != other_array    

    #testing iter
    def test_iter_like_example(self):
        array = Array.from_list(['zero', 'one', 'two', 'three', 'four'])
        test_list = []
        for item in array: 
            test_list.append(item)
        assert Array.from_list(test_list) == array

            
    #testing reversed
    def test_reversed_like_example(self):
        test_array = Array.from_list(['zero', 'one', 'two', 'three', 'four'])
        test_list = []

        for item in reversed(test_array):
            test_list.append(item)
        assert Array.from_list(test_list) == Array.from_list(['four', 'three', 'two', 'one', 'zero'])
            

    #testing delitem
    def test_delitem_negative_index(self):
        test_array = Array(7)
        with pytest.raises(IndexError):
            test_array.__delitem__(-5)

    def test_delitem_index_too_big(self):
        test_array = Array(7)
        with pytest.raises(IndexError):
            test_array.__delitem__(100)

    def test_delitem_deletes(self):
        test_array = Array.from_list(['zero', 'one', 'two'])
        del test_array[1]
        assert test_array == Array.from_list(['zero', 'two'])

    def test_delitem_first_entry(self):
        test_array = Array.from_list(['one', 'two', 'three', 'four'])
        test_array.__delitem__(0)
        assert list(test_array) == ['two', 'three', 'four']

    def test_delitem_last_entry(self):
        test_array = Array.from_list(['one', 'two', 'three', 'four'])
        test_array.__delitem__(3)
        assert list(test_array) == ['one', 'two', 'three']

    def test_delitem_empty_array(self):
        test_array = Array(0)
        with pytest.raises(IndexError):
            test_array.__delitem__(0)

    #testing contains
    def test_contains_does_contain(self):
        test_array = Array.from_list(['one', 'two', 'three', 'four'])
        assert 'three' in test_array

    def test_contains_does_not_contain(self):
        test_array = Array.from_list(['one', 'two', 'three', 'four'])
        with pytest.raises(AssertionError):
            assert 'five' in test_array


    #testing does_not_contain
    def test_does_not_contain_and_does_not(self):
        test_array = Array.from_list(['one', 'two', 'three', 'four'])
        assert 'five' not in test_array

    def test_does_not_contain_but_does(self):
        test_array = Array.from_list(['one', 'two', 'three', 'four'])
        with pytest.raises(AssertionError):
            assert 'one' not in test_array


    #testing clear
    def test_clear_does_anything(self):
        test_array = Array(5)
        test_array.clear()
        assert test_array == Array(0)
            

    #testing str
            

    #testing repr