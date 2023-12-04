# Описать функцию InvertDigits(К), меняющую порядок следования цифр целого положительного числа К
# на обратный (К -- параметр целого типа, являющийся одновременно входным и выходным).
# С помощью этой функции поменять порядок следования цифр на обратный для каждого из пяти данных целых чисел.
def InvertDigits(K):
    reversed_number = int(str(K)[::-1])
    return reversed_number

numbers = [12345, 6789, 54321, 98765, 123456789]
for num in numbers:
    inverted_num = InvertDigits(num)
    print(f"Original:{num}, Inverted:{inverted_num}")
