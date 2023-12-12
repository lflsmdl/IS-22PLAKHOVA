# Дан список ненулевых целых чисел размера N. Проверить, чередуются ли в нем положительные и отрицательные числа. 
# Если чередуются, то вывести 0, если нет, то вывести порядковый номер первого элемента, нарушающего закономерность.
def check_alternating(numbers):
    for i in range(1, len(numbers)):
        if (numbers[i] > 0 and numbers[i-1] > 0) or (numbers[i] < 0 and numbers[i-1] < 0):
            return i
    return 0

arr = [1, -2, 3, -4, 5, -6]
result = check_alternating(arr)
print(result)
