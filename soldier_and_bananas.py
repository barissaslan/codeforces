k, n, w = [int(x) for x in input().split()]
cost = 0

for i in range(1, w + 1):
    cost += i * k

if cost > n:
    print(cost - n)
else:
    print(0)
