# Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной последовательности из
# целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:
# Элементы первого и второго файлов:
# Элементы первого файла, отсутствующие во втором:
# Элементы второго файла, отсутствующие в первом:
# Количество элементов
# Индекс первого минимального элемента
# Индекс последнего максимального элемента

polozhit = ['99 6 12 38 20 45 100 15']
f1 = open('data_1.txt', 'w')
f1.writelines(polozhit)
f1.close()

otric = ['-9 -40 -22 -36 -25 -43 -101 -18']
f2 = open('data_2.txt', 'w')

all_el = polozhit + otric
colvo = len(polozhit) + len(otric)

print(all_el)