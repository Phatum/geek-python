"""
Задание №2

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""

time = int(input("Введите время в секундах >>> "))
hour = time // 60 // 60
minute = time // 60
while minute >= 60:
    minute = minute - 60
else:
    second = time
    while second >= 60:
        second = second - 60
    else:
        print(f"{hour}:{minute}:{second}")
