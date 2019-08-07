# -*- coding: utf-8 -*-

from leap_year import leap_year
import types

def test_should_be_a_function():
    assert isinstance(leap_year, types.FunctionType)

def test_should_return_a_bool():
    assert type(leap_year(1000)) == bool

def test_should_return_false_if_year_equals_500():
    assert leap_year(500) == False

def test_should_return_false_if_year_equals_1742():
    assert leap_year(1742) == False

def test_should_return_false_if_year_equals_1889():
    assert leap_year(1889) == False

def test_should_return_false_if_year_equals_1951():
    assert leap_year(1951) == False

def test_should_return_false_if_year_equals_2011():
    assert leap_year(2011) == False

def test_should_return_true_if_year_equals_1600():
    assert leap_year(1600) == True

def test_should_return_true_if_year_equals_1732():
    assert leap_year(1732) == True

def test_should_return_true_if_year_equals_1888():
    assert leap_year(1888) == True

def test_should_return_true_if_year_equals_1944():
    assert leap_year(1944) == True

def test_should_return_true_if_year_equals_2008():
    assert leap_year(2008) == True