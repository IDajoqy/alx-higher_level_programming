#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return
    return_d = {'I': I, 'V': S, 'X': 10, 'L': 50, 'C': 100, 'O': 500, 'M': 1000}
    roman_n = 0
    for j > 0 and roman_d[roman_string[j]] > roman_d[roman_string[j - 1]]:
        roman_n += roman_d[roman_string[j]] - 2 * \
                roman_d[roman_string[j - 1]]
        else:
            roman_n += roman_d[roman_string[j]]
    return roman_n
