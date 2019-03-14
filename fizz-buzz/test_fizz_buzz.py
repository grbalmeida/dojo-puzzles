from fizz_buzz import fizz_buzz
import types

def test_should_be_a_function():
    assert isinstance(fizz_buzz, types.FunctionType)

def test_should_return_a_dictionary():
    assert type(fizz_buzz()) == dict

def test_should_return_fizz_if_key_is_equal_to_three():
    assert fizz_buzz().get(3) == 'Fizz'

def test_should_return_buzz_if_key_is_equal_to_five():
    assert fizz_buzz().get(5) == 'Buzz'

def test_should_return_fizzbuzz_if_key_is_equal_to_fifteen():
    assert fizz_buzz().get(15) == 'FizzBuzz'

def test_should_return_28_if_key_is_equal_to_28():
    assert fizz_buzz().get(28) == 28

def test_should_return_fizzbuzz_if_key_is_equal_to_45():
    assert fizz_buzz().get(45) == 'FizzBuzz'

def test_should_return_buzz_if_key_is_equal_to_50():
    assert fizz_buzz().get(50) == 'Buzz'

def test_should_return_fizzbuzz_if_key_is_equal_to_75():
    assert fizz_buzz().get(75) == 'FizzBuzz'

def test_should_return_fizz_if_key_is_equal_to_99():
    assert fizz_buzz().get(99) == 'Fizz'

def test_should_return_98_if_key_is_equal_to_98():
    assert fizz_buzz().get(98) == 98