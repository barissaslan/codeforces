rounds = int(input())

mishka_score = chris_score = 0

for i in range(rounds):
    m, c = input().split()
    if m > c:
        mishka_score += 1
    elif m < c:
        chris_score += 1

if mishka_score > chris_score:
    print("Mishka")
elif mishka_score < chris_score:
    print("Chris")
else:
    print("Friendship is magic!^^")
