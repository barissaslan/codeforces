number_of_groups = int(input())
number_of_childrens = [int(x) for x in input().split()]

one = two = three = four = 0
number_of_taxis = 0

for children in number_of_childrens:
    if children is 1:
        one += 1
    elif children is 2:
        two += 1
    elif children is 3:
        three += 1
    else:
        four += 1

number_of_taxis += four
if two is not 0:
    number_of_taxis += (two // 2)
    if two % 2 == 0:
        two = 0
    else:
        two = 1

if one < three:
    number_of_taxis += one
    three -= one
    number_of_taxis += three
    if two is 1:
        number_of_taxis += 1
elif one > three:
    number_of_taxis += three
    one -= three
    number_of_taxis += (one // 4)
    one -= (one // 4) * 4
    if one is 3 and two is 1:
        number_of_taxis += 2
    elif one is 0 and two is 0:
        number_of_taxis += 0
    elif one is not 0 or two is not 0:
        number_of_taxis += 1
else:
    number_of_taxis += one
    if two is 1:
        number_of_taxis += 1

print(number_of_taxis)

