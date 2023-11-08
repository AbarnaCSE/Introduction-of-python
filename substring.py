X = input("Enter First string:")
Y = input("Enter Second string:")
m = len(X)
n = len(Y)
sub = [[0 for i in range(n + 1)] for j in range(m+1)]
result =0
for i in range(m+1):
    for j in range(n+1):
        if(i==0 or j==0):
            sub[i][j] = 0
        elif(X[i-1] == Y[j-1]):
            sub[i][j] = sub[i-1][j-1]+1
            result = max(result,sub[i][j])
        else:
            sub[i][j] = 0            
print("Length:",sub[i][j])                