def Add(numbers):
    if numbers == '':
        return 0
    if len(numbers) == 1:
        return int(numbers)
    result = 0
    for number in numbers.split(','):
        result += int(number)
    return result