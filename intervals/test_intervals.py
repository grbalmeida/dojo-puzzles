# -*- coding: utf-8 -*-

from intervals import intervals
import types

def test_should_be_a_function():
    assert isinstance(intervals, types.FunctionType)

def test_should_return_an_empty_list_if_an_empty_list_is_passed():
    assert intervals([]) == []

def test_should_remove_duplicate_values():
    assert intervals([1, 1, 1]) == [[1]]
    assert intervals([1, 1, 1, 2, 3, 4, 4, 4, 5, 8, 12, 12]) == [[1, 5], [8], [12]]
    assert intervals([8, 90, 91, 91, 92, 95]) == [[8], [90, 92], [95]]

def test_should_return_list_with_one_list():
    assert intervals([1]) == [[1]]
    assert intervals([1, 2]) == [[1, 2]]
    assert intervals([1, 2, 3]) == [[1, 3]]
    assert intervals([3, 4, 5]) == [[3, 5]]
    assert intervals([11, 12, 13, 14, 15]) == [[11, 15]]

def test_should_return_a_list_with_two_lists():
    assert intervals([1, 2, 7, 8]) == [[1, 2], [7, 8]]
    assert intervals([1, 2, 10]) == [[1, 2], [10]]
    assert intervals([1, 50]) == [[1], [50]]

def test_should_return_a_list_with_three_list():
    assert intervals([1, 2, 4, 5, 6, 7, 10, 11]) == [[1, 2], [4, 7], [10, 11]]
    assert intervals([10, 11, 12, 14, 27]) == [[10, 12], [14], [27]]

def test_should_return_a_list_with_four_lists():
    input = [100, 101, 102, 103, 104, 105, 110, 111, 113, 114, 115, 150]
    output = [[100, 105], [110, 111], [113, 115], [150]]

    assert intervals(input) == output