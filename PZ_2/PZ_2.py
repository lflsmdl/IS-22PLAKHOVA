#С начала суток прошло N секунд (N - целое). Найти количество секунд, прошедших с начала последней минуты
while True:
    try:
        n = int(input("Введите количетсво секунд: "))
        seconds_since_last_minute = n % 60
        print("С начала последней минуты прошло", seconds_since_last_minute, "секунд")
        break
    except ValueError:
        print('Ошибка! Введите целое число')
