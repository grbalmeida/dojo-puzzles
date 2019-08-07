# -*- coding: utf-8 -*-

def leap_year(year):
    is_divisible_by_4 = year % 4 == 0
    is_divisible_by_400 = year % 400 == 0
    is_divisible_by_100 = year % 100 == 0

    return is_divisible_by_4 and (not is_divisible_by_100 or is_divisible_by_400)