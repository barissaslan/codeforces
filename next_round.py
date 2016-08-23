n, k = [int(x) for x in input().split()]

scores = [int(x) for x in input().split()]
k_score = scores[k - 1]
numbers_of_advance = 0

for score in scores:
    if score >= k_score and not score == 0:
        numbers_of_advance += 1
    else:
        break

print(numbers_of_advance)

