def Add(numbers):
    if numbers == '':
        return 0
    if len(numbers) == 1:
        return int(numbers)
    return sum([int(number) for number in numbers.split(',')])