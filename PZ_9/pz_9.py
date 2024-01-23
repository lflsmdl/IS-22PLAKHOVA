# Дана строка '2020год -16 -10 -6 4 20 32 36 32 32 15 1 -15', отражающая средние температуры по месяцам в году.
# Преобразовать информацию из строки в словарь, с использованием функции найти среднюю
# и минимальные температуры, результаты вывести на экран.
def average_temperatures(temp_string):
    temp_list = temp_string.split()
    temp_dict = {
        'январь': int(temp_list[1]),
        'февраль': int(temp_list[2]),
        'март': int(temp_list[3]),
        'апрель': int(temp_list[4]),
        'май': int(temp_list[5]),
        'июнь': int(temp_list[6]),
        'июль': int(temp_list[7]),
        'август': int(temp_list[8]),
        'сентябрь': int(temp_list[9]),
        'октябрь': int(temp_list[10]),
        'ноябрь': int(temp_list[11]),
        'декабрь': int(temp_list[12])
    }
    average_temp = sum(temp_dict.values()) / len(temp_dict)
    min_temp = min(temp_dict.values())
    return average_temp, min_temp
temp_string = '2020год -16 -10 -6 4 20 32 36 32 32 15 1 -15'
average, minimum = average_temperatures(temp_string)
print('Средняя температура:', average)
print('Минимальная температура:', minimum)