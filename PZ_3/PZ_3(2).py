#Даны целые числа a, b, c. Проверить истинность высказывания: "Существует треугольник со сторонами a, b, c."
a = int(input("Введите сторону a: "))
b = int(input("Введите сторону b: "))
c = int(input("Введите сторону c: "))
if a + b > c and a + c > b and b + c > a:
    print("Треугольник со сторонами {}, {}, и {} существует".format(a, b, c))
else:
    print("Треугольник со сторонами {}, {}, и {} не существует".format(a, b, c))