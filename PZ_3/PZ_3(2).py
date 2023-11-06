#Даны целые числа a, b, c. Проверить истинность высказывания: "Существует треугольник со сторонами a, b, c."
while True:
    try:
        a = float(input("Введите сторону a: "))
        b = float(input("Введите сторону b: "))
        c = float(input("Введите сторону c: "))
        if a + b > c and a + c > b and b + c > a:
            print("Треугольник со сторонами {}, {}, и {} существует".format(a, b, c))
        else:
            print("Треугольник со сторонами {}, {}, и {} не существует".format(a, b, c))
        break
    except ValueError:
        print('Ошибка! Введите число')