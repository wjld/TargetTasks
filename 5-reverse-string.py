s = input("insert string to be inverted: ")

#print(s[::-1])
for i in range(len(s)):
    print(s[len(s) - i - 1], end='')
print()