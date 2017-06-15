y = int(input())


def is_distinct(num:int):
    s = [c for c in str(num)]
    for i in range(10):
        if s.count(str(i)) > 1:
            return False
    return True


while True:
    y += 1
    if is_distinct(y):
        print(y)
        break
