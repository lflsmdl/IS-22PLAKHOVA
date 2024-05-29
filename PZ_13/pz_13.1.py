# В матрице найти среднее арифметическое положительных элементов.
import random
matrix = [[random.randint(-10, 10) for _ in range(3)] for _ in range(3)]
for row in matrix:
    print(row)
positivelem = [elem for row in matrix for elem in row if elem > 0]
averagepositive = sum(positivelem) / len(positivelem) if positivelem else 0
print(f"Среднее арифметическое положительных элементов:{averagepositive:.2f}")