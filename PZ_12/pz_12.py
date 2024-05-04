# В последовательности их N чисел (N - четное) во второй eе половине найти сумму
# элементов больших 10.

def sumNmore10(sequence):
    half_len = len(sequence) // 2
    for num in sequence[half_len:]:
        if num > 10:
            yield num


numbers = [8, 12, 6, 16, 2, 14]

result = sum(sumNmore10(numbers))
print(result)