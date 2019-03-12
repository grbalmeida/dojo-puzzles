# -*- coding: utf-8 -*-

from jokenpo import jokenpo
import types

def test_should_be_a_function():
    assert isinstance(jokenpo, types.FunctionType)

def test_should_return_a_string():
    assert type(jokenpo('Pedra', 'Pedra')) == str

def test_should_return_an_error_message_if_is_an_invalid_option():
    assert jokenpo('Alumínio', 'Pedra') == 'Opção inválida'

def test_should_return_a_draw():
    assert jokenpo('Pedra', 'Pedra') == 'Empate'

def test_should_stone_win_the_game():
    assert jokenpo('Pedra', 'Tesoura') == 'Ganhador: Pedra'

def test_should_scissors_win_the_game():
    assert jokenpo('Tesoura', 'Papel') == 'Ganhador: Tesoura'

def test_should_paper_win_the_game():
    assert jokenpo('Papel', 'Pedra') == 'Ganhador: Papel'

def test_reverse_test():
    assert jokenpo('Pedra', 'Papel') == 'Ganhador: Papel'