# a = range(1, 21)
# for i in a:
#     print(i)
#


# a = range(3, 31, 3)
# for z in a:
#     print(z)
#

# age = int(input())
# print(age)
# if age < 2:
#     print("Младенец")
# elif age >= 2 and age < 4:
#     print("Малыш")
# elif age >= 4 and age < 13:
#     print("Ребенок")
# elif age >= 13 and age < 20:
#     print("Подросток")
# elif age >= 20 and age < 65:
#     print("Взрослый")
# elif age >= 65:
#     print("Пожилой человек")
#     ##
#


# nk = ('Словарь Python может содержать как несколько пар «ключ-значение», так и миллионы таких пар. '
#       'Поскольку словарь может содержать большие объемы данных, Python предоставляет средства для перебора элементов словаря. '
#       'Информация может храниться в словарях по-разному, поэтому предусмотрены разные способы перебора. '
#       'Программа может перебрать все пары «ключ-значение» в словаре, только ключи или только значения.')
# dict = {}
# for n in nk:
#     dict[n.lower()] = nk.count(n)
# del dict[' ']
# print(dict)

a = int(input("Введите число:"))
operation = input("Операция:")
b = int(input("Введите число:"))

if operation == "+":
    print(a + b)
elif operation == "-":
    print(a - b)
elif operation == "*":
    print(a * b)
elif operation == "/":
    if a != 0:
        print(a / b)



