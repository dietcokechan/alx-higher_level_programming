#!/usr/bin/python3
def roman_to_int(roman_string):
    sum = 0
    if roman_string and isinstance(roman_string, str):
        roman = {'D': 500, 'C': 100, 'M': 1000,
                'L': 50, 'X': 10, 'V': 5, 'I': 1}
        rlist = [roman.get(i) for i in roman_string]
        for i, char in enumerate(rlist):
            if i < len(rlist) - 1:
                if rlist[i + 1] > char:
                    sum -= char
                else:
                    sum += char
            else:
                sum += char
    return sum
