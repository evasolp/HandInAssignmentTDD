class NegativeError(Exception):
    def __init__(self, negative_numbes):
        print('Negatives not allowed: ' + negative_numbes[:-1])

def Add(numbers):
    if numbers == '':
        return 0
    if len(numbers) == 1:
        return int(numbers)
    number = ''
    numbers_list = []
    negative_numbers = ''
    for symbol in numbers:
        if symbol.isdigit() or symbol == '-':
            number += symbol
        else:
            if 1 <= len(number) < 4 or number == '1000':
                if number[0] == '-':
                    negative_numbers += number + ','
                else:
                    numbers_list.append(int(number))
            number = '' 
    if 1 <= len(number) < 4 or number == '1000':
        numbers_list.append(int(number))
    if negative_numbers != '':
        raise NegativeError(negative_numbers)
    return sum(numbers_list)

print(Add('1\n2,3'))