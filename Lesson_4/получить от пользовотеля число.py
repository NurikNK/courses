# # integer = int(input())
# # if integer %2 == 0:
# #     print("Even number")
# # else:
# #     print("Odd number")
#
# integer = int(input("Enter number:"))
# if integer > 0:
#     print("Pasitive number")
# elif integer == 0:
#     print("Zerro number")
# else:
#     print("Negative number")


 #Определить регистр первого символа в строке
#
# name = input("Enter name:")
# if name[0].isupper():
#     print("First letter in lower case")
#     print("first letter in upper case")
# else:
# Найти разность всех чисел

integers = [100, 50, 25, 10]
difference = 0
for i, number in enumerate(integers):
    if i == 0:
        difference = number
    else:
        difference = difference - number

print("Difference:", difference)

