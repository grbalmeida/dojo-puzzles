# -*- coding: utf-8 -*-

from cash_machine import cash_machine
import types

def test_should_be_a_function():
    assert isinstance(cash_machine, types.FunctionType)

def test_should_return_an_error_message_if_value_is_negative():
    assert cash_machine(-10) == 'Informe um valor positivo'

def test_should_return_an_error_message_if_value_is_less_than_10():
    assert cash_machine(9) == 'Saque um valor acima de 10 reais'

def test_should_return_an_error_message_if_number_is_not_divisible_by_10():
    assert (cash_machine(11)) == 'Informe um valor válido para o saque'

def test_should_return_a_list_with_an_item():
    assert len(cash_machine(10)) == 1

def test_should_return_a_note_of_10():
    cash = cash_machine(10)
    assert len(cash) == 1 and cash.count(10) == 1

def test_should_return_a_note_of_20():
    assert cash_machine(20) == [20]

def test_should_return_a_note_of_20_and_a_note_of_10():
    assert cash_machine(30) == [20, 10]

def test_should_return_a_note_of_50_and_a_note_of_10():
    assert cash_machine(60) == [50, 10]

def test_should_return_a_note_of_50_and_a_note_of_20_and_a_note_of_10():
    assert cash_machine(80) == [50, 20, 10]

def test_should_return_a_note_of_100_and_a_note_of_20():
    assert cash_machine(120) == [100, 20]

def test_should_return_3_notes():
    assert cash_machine(170) == [100, 50, 20]

def test_should_return_2_notes_of_100():
    assert cash_machine(200) == [100, 100]

def test_should_return_10_notes_of_100():
    cash = cash_machine(1000)
    assert len(cash) == 10 and cash.count(100) == 10

def test_should_return_18_notes():
    cash = cash_machine(1590)
    assert len(cash) == 18 and cash.count(100) == 15 and cash.count(50) == 1 and cash.count(20) == 2
