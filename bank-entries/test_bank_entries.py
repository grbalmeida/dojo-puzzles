# -*- coding: utf-8 -*-

from bank_entries import bank_entries
import types

def test_should_be_a_function():
    assert isinstance(bank_entries, types.FunctionType)

def test_should_return_a_dictionary():
    assert type(bank_entries('123')) == dict 

def test_should_return_a_dictionary_with_the_key_is_valid_check_in():
    assert 'is_valid_check_in' in bank_entries('123')

def test_should_return_a_dictionary_with_the_key_is_valid_entry_time():
    assert 'is_valid_entry_time' in bank_entries('123')

def test_should_is_valid_check_in_key_to_be_a_bool():
    assert type(bank_entries('123').get('is_valid_check_in')) == bool

def test_should_is_valid_entry_time_key_to_be_a_bool():
    assert type(bank_entries('123').get('is_valid_entry_time')) == bool

def test_should_is_valid_check_in_to_be_false():
   assert bank_entries('123').get('is_valid_check_in') == False
   assert bank_entries('ABC').get('is_valid_check_in') == False
   assert bank_entries('[ABCD-10-FG 23:59:59] - Abertura da Porta OK').get('is_valid_check_in') == False
   assert bank_entries('[2099-32-32 25:59:59] - Abertura da Porta OK').get('is_valid_entry_time') == False

def test_should_is_valid_check_in_to_be_true():
    assert bank_entries('[2010-10-12 23:59:59] - Abertura da Porta OK').get('is_valid_check_in') == True
    assert bank_entries('[1990-12-20 10:02:10] - Abertura da Porta OK').get('is_valid_check_in') == True
    assert bank_entries('[2004-02-18 05:05:10] - Abertura da Porta OK').get('is_valid_check_in') == True

def test_should_is_valid_entry_time_to_be_false():
    assert bank_entries('[2010-10-12 23:59:59] - Abertura da Porta OK').get('is_valid_entry_time') == False
    assert bank_entries('[2010-10-12 19:59:59] - Abertura da Porta OK').get('is_valid_entry_time') == False
    assert bank_entries('[2010-10-12 08:59:59] - Abertura da Porta OK').get('is_valid_entry_time') == False
    assert bank_entries('[2099-99-99 10:59:59] - Abertura da Porta OK').get('is_valid_entry_time') == False

def test_should_is_valid_entry_time_to_be_true():
    assert bank_entries('[2010-10-12 10:59:59] - Abertura da Porta OK').get('is_valid_entry_time') == True
    assert bank_entries('[2010-10-12 11:59:59] - Abertura da Porta OK').get('is_valid_entry_time') == True
    assert bank_entries('[2010-10-12 15:59:59] - Abertura da Porta OK').get('is_valid_entry_time') == True