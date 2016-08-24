number_of_statements = int(input())
x = 0
for i in range(number_of_statements):
    if '+' in input():
        x += 1
    else:
        x -= 1

print(x)