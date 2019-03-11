def simple_statistics(numbers):
    minimum_value = 0
    maximum_value = 0
    number_of_elements = 0
    average_value = 0
    sum_of_numbers = 0

    for index, number in enumerate(numbers):
        if(index == 0 or minimum_value > number):
            minimum_value = number
        if(number > maximum_value):
            maximum_value = number
        number_of_elements += 1 
        sum_of_numbers += number

    if len(numbers) > 0:
        average_value = sum_of_numbers / len(numbers) 

    statistics = {
        'minimum_value': minimum_value,
        'maximum_value': maximum_value,
        'number_of_elements': number_of_elements,
        'average_value': average_value
    }

    return statistics