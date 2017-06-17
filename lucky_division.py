import itertools

num = input()


def get_all_combination(repeat):
    list_of_lucky = []
    for string in itertools.product('47', repeat=repeat):
        lucky = ''.join(string)
        list_of_lucky.append(lucky)
    return list_of_lucky


if num in get_all_combination(len(num)):
    print('YES')
else:
    find = False
    for i in range(1, len(num) + 1):
        for com in get_all_combination(i):
            if int(num) % int(com) == 0:
                print('YES')
                find = True
                break
        if find:
            break

    if not find:
        print('NO')
