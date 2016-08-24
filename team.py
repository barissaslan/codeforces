number_of_problems = int(input())
number_of_implements = 0

for i in range(number_of_problems):
    ones = [x for x in input().split() if int(x) == 1]
    if len(ones) > 1:
        number_of_implements += 1

print(number_of_implements)