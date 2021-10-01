"""def print_hello(name):
    print(f"hello {name}")
    print(f"Привет {name}")

name = "Игорь", "Артем"
print_hello(name[1]) #вывести приветствие с именем


num = [1, 2, 3]
print(len(num)) список -> длина списка
print(3)
len(num) = 3
print_hello(name[0])
print() #печатает
input()
int()
float()
str()
range()

#def print_hello():

def sum(a, b):
    sum = a + b # sum = 5
    ....
    
    if 1 условие:
        return одно 
    if 2 условие:
        return второе
    if 3 условие: 
        return второе

a = 2
b = 3
c = sum(a, b)
print(c)
"""

def sum(a, b):
    return a + b

def dif(a, b):
    return a - b

#print(f"Сумма: {sum(9, 2)}\nРазность: {dif(5, 3)}")
#print(sum(9, 2), dif(5, 3), sep="%", end="")
#mul()
#float_div() 15 / 2 = 7.5
#int_div() 15 // 2 = 7

name = "Artem"
lst = [1, 2, 3, 4, 5, 6]
tpl = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(len(name))
print(len(lst))
print(len(tpl))

def length(natasha):
    counter = 0
    for i in natasha:
        counter += 1
    return counter

print(length(name))
print(length(lst))
print(length(tpl))



def find_max(a, b, c):


print(find_max(1, 2, 3))