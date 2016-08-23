number_of_lines = int(input())

words = []

for i in range(number_of_lines):
    line = input()
    if len(line) > 10:
        line = line[0] + str(len(line) - 2) + line[-1]
    words.append(line)

for word in words:
    print(word)

