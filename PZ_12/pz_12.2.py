# Составить генератор (yield), который выводит из строки только буквы.

import string
def get_letters(input_string):
    for a in input_string:
        if a.isalpha():
            yield a

input_str = "abc123def456"
letters_generator = get_letters(input_str)

for letter in letters_generator:
    print(letter)
