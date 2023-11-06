#Даны целые числа a, b, c. Проверить истинность высказывания: "Существует треугольник со сторонами a, b, c."
while True:
    try:
        a = int(input("Введите сторону a: "))
        b = int(input("Введите сторону b: "))
        c = int(input("Введите сторону c: "))
        if a + b > c and a + c > b and b + c > a:
            print("True")
        else:
            print("False")
        break
    except ValueError:
        print('Ошибка! Введите целое число.')