n, m, a = [int(x) for x in input().split()]

if n % a == 0:
    if m % a == 0:
        f = (n // a) * (m // a)
    elif m > a:
        f = (n // a) * ((m // a) + 1)
    else:
        f = (n // a)
elif n > a:
    if m % a == 0:
        f = ((n // a) + 1) * (m // a)
    elif m > a:
        f = ((n // a) + 1) * ((m // a) + 1)
    else:
        f = ((n // a) + 1)
else:
    if m % a == 0:
        f = m // a
    elif m > a:
        f = (m // a) + 1
    else:
        f = 1

print(f)
