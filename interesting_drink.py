number_of_shops = int(input())
prices_of_bottles = (int(x) for x in input().split())
number_of_days = int(input())
coins_of_Vasilly = []
for x in range(number_of_days):
    coins_of_Vasilly.append(int(input()))

for coins in coins_of_Vasilly:
    number_of_able = 0
    for price in prices_of_bottles:
        if coins >= price:
            number_of_able += 1
    print(number_of_able)
