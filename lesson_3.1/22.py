def sum_list_numbers(numbers: list) -> float:
    result = 0
    for number in numbers:
        result += number
    return result

def reverse_list(numbers: list) -> list:
    i = len(numbers) - 1
    reverse_list = []
    while i >= 0:
        reverse_list.append(numbers[i])
        i -= 1
    return reverse_list
nums = [10, 20, 30, 40, 50]

result = reverse_list(nums)
print(result)