hate = 'I hate'
love = 'I love'
output = ''
layer = int(input())

for i in range(1, layer + 1):
    if i % 2 == 1:
        if i < layer:
            output += hate + ' that '
        else:
            output += hate + ' it'
    else:
        if i < layer:
            output += love + ' that '
        else:
            output += love + ' it'

print(output)
