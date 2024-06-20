numbers = [1, 2, 3]


def my_list(numbers):
    numbers.append(4)
    numbers[0] = 100
    return numbers


l = my_list(numbers)
print(l)
