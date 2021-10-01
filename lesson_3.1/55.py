def max_list_numbers(numbers: list) -> float:
    result = 0
    for number in numbers:
     if number < result:
      result = number
    return result
nums = [10, 20, 30, 40, 50]
print(max_list_numbers(nums))
