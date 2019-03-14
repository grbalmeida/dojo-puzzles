def fizz_buzz():
    dictionary = {}

    for number in range(1, 100):
        if number % 3 == 0 and number % 5 == 0:
            dictionary[number] = 'FizzBuzz'
        elif number % 3 == 0:
            dictionary[number] = 'Fizz'
        elif number % 5 == 0:
            dictionary[number] = 'Buzz'
        else:
            dictionary[number] = number
    
    return dictionary