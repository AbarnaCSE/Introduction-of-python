string = input("Enter string:")
a = ""
for i in string:
    if i not in a:
        a += i
print(len(a))

