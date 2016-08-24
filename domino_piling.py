n, m = [int(x) for x in input().split()]

if n % 2 == 0:
    f = (n // 2) * m
elif m % 2 == 0:
    f = n * (m // 2)
else:
    f = m * (n // 2) + (m // 2)

print(f)