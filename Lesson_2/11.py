numbers = [1, 2, 3, 4, 5, 5, 8, 5, 8, 9, 7]
numbers_1 = [10, 20, 30, 100]

numbers.append(6)
numbers.reverse()

numbers.append("Nurik")
numbers.remove("Nurik")
numbers.pop(10)
numbers.sort()

numbers.extend(numbers_1)

numbers.insert(3, 11)
print(numbers)
