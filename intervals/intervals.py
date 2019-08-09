# -*- coding: utf-8 -*-

def get_unique(values):
    new_list = []

    for value in values:
        if value not in new_list:
            new_list.append(value)

    return new_list

def intervals(list):
    if len(list) == 0:
        return list

    list = get_unique(list)
    current_list = []
    new_list = []
    current_value = list[0]

    for index in range(len(list)):
        if list[index] == current_value:
            current_list.append(list[index])

            try:
                current_value = list[index + 1]
            except:
                current_value = None

        if not list[index] + 1 == current_value or current_value == None:
            if len(current_list) == 1 or len(current_list) == 2:
                new_list.append(current_list)
            elif len(current_list) > 2:
                new_list.append([current_list[0], current_list.pop()])
            
            current_list = []

    return new_list