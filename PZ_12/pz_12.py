# В последовательности их N чисел (N - четное) во второй eе половине найти сумму
# элементов больших 10.

numbers = [8, 12, 6, 16, 2, 14]
polovina = len(numbers) // 2
bol_ten = [i for i in numbers[polovina:] if i > 10]
result = sum(bol_ten)
print(result)