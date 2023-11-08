string = input("Enter the string:")
result = {}
for i in string:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1
result = max(result, key = result.get)        
print("The most frequent character is:",result)        