# -*- coding: utf-8 -*-

def jokenpo(first_player, second_player):
    valid_options = ['Pedra', 'Papel', 'Tesoura']
    played_options = [first_player, second_player]
    
    if valid_options.count(first_player) == 0 or valid_options.count(second_player) == 0:
        return 'Opção inválida'

    if first_player == second_player:
        return 'Empate'

    if played_options.count('Pedra') == 1 and played_options.count('Tesoura') == 1:
        return 'Ganhador: Pedra'

    if played_options.count('Tesoura') == 1 and played_options.count('Papel') == 1:
        return 'Ganhador: Tesoura'

    if played_options.count('Papel') == 1 and played_options.count('Pedra') == 1:
        return 'Ganhador: Papel'