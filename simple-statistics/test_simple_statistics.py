from simple_statistics import simple_statistics
import types

def test_should_be_a_function():
    assert isinstance(simple_statistics, types.FunctionType)

def test_should_return_a_dictionary():
    assert type(simple_statistics([])) == dict

def test_should_return_a_dictionary_with_the_key_minimum_value():
    assert 'minimum_value' in simple_statistics([])

def test_should_return_a_dictionary_with_the_key_maximum_value():
    assert 'maximum_value' in simple_statistics([])

def test_should_return_a_dictionary_with_the_key_number_of_elements():
    assert 'number_of_elements' in simple_statistics([])

def test_should_return_a_dictionary_with_the_key_average_value():
    assert 'average_value' in simple_statistics([])

def test_should_return_the_key_minimum_value_equal_to_zero():
    assert simple_statistics([]).get('minimum_value') == 0

def test_should_return_the_key_maximum_value_equal_to_zero():
    assert simple_statistics([]).get('maximum_value') == 0

def test_should_return_the_key_number_of_elements_equal_to_zero():
    assert simple_statistics([]).get('number_of_elements') == 0

def test_should_return_the_key_average_value_equal_to_zero():
    assert simple_statistics([]).get('average_value') == 0

def test_should_return_minimum_value_equal_to_two_negative():
    assert simple_statistics([6, 9, 15, -2, 92, 11]).get('minimum_value') == -2

def test_should_return_maximum_value_equal_to_92():
    assert simple_statistics([6, 9, 15, -2, 92, 11]).get('maximum_value') == 92

def test_should_return_number_of_elements_equal_to_6():
    assert simple_statistics([6, 9, 15, -2, 92, 11]).get('number_of_elements') == 6

def test_should_return_average_value_equal_to_18():
    assert simple_statistics([10, 20, 48, 5, 7]).get('average_value') == 18