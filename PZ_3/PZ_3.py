#Даны числа x, y. Проверить высказывания: "Точка с координатами (x, y) лежит в чевертой координатной четверти.
while True:
    try:
        x = float(input("Введите x: "))
        y = float(input("Введите y: "))
        if  x > 0 and y < 0:
            print("True")
        else:
            print("False")
        break
    except ValueError:
        print('Ошибка! Введите число')