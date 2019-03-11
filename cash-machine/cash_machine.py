# -*- coding: utf-8 -*-

def error_messages(value_taken):
    error_messages = []
    
    if value_taken < 0:
        error_messages.append('Informe um valor positivo')
    if value_taken < 10:
        error_messages.append('Saque um valor acima de 10 reais')
    if value_taken % 10 != 0:
        error_messages.append('Informe um valor válido para o saque')

    return error_messages

def cash_machine(value_taken):
    if len(error_messages(value_taken)) > 0:
        return error_messages(value_taken)[0]

    available_notes = [100, 50, 20, 10]
    returned_notes = []

    for index, note in enumerate(available_notes):
        while value_taken != 0 and value_taken >= available_notes[index]:
            returned_notes.append(available_notes[index])
            value_taken -= available_notes[index]
    
    return returned_notes