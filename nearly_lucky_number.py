import itertools


def get_all_combination(repeat):
    list_of_lucky = []
    for string in itertools.product('47', repeat=repeat):
        lucky = ''.join(string)
        list_of_lucky.append(lucky)
    return list_of_lucky


num = input()

num_of_lucky_digit = len([digit for digit in num if digit in '47'])

repeat = len(str(num_of_lucky_digit))

if str(num_of_lucky_digit) in get_all_combination(repeat):
    print('YES')
else:
    print('NO')
