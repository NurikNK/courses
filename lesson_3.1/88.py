# def chop(t):
#
#     t.pop(0)
#     t.pop(-1)
#     return t
# t = [1, 2, 3, 4, 5]
# print(chop(t))
#
"""
# Отпуск мечты: напишите программу, которая опрашивает пользователей, где бы они хотели провести отпуск. Включите блок кода для вывода результатов опроса.
# Пример вывода: ключом будет номер цикла, значением ввод пользователя
# {0:  ‘Milan’ , 1:  ‘Paris’} ("""
# ""
# мальдивы
# Париж
# Сочи
# шейдшели
# мальдивы
# Париж
# Сочи
# шейдшели
# {2:шейдшели
#  2:Сочи
#  3:Париж}
""


cities = set()
while True:
    city = input()
    if city == "end":
        break
    cities.add(city)
cities_result = dict()
counter = 0
for i in cities:
    cities_result[counter] = i
    counter +=1
print(cities_result)

