# Составить программу, в которой функцию построит изображение, в котором в первой строке 1 звездочка, во второй - 2,
# в третьей - 3, ..., в строке с номером m - m звездочек.
while True:
    try:
        rows = int(input("Введите количество строк: "))


        def build_image(rows):
            for i in range(1, rows + 1):
                print('*' * i)
        build_image(rows)
        break

    except ValueError:
        print('Ошибка! Введите целое число.')
