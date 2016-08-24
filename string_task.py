vowels = ("a", "o", "y", "e", "u", "i")
string = input().lower()
new_string = ""

for char in string:
    if char not in vowels:
        new_string += "." + char
print(new_string)