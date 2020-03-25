def Add(numbers):
    if numbers == '':
        return 0
    if len(numbers) == 1:
        return int(numbers)
    number = ''
    numbers_list = []
    for symbol in numbers:
        if symbol.isdigit():
            number += symbol
        else:
            if number != '':
                numbers_list.append(int(number))
                number = '' 
    if number != '':
        numbers_list.append(int(number))
    return sum(numbers_list)

print(Add('1\n2,3'))