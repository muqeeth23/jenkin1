
X = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[1,0,0],
    [0,1,0],
    [0,0,1]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

print(len(X))
print(len(Y[0]))
print(len(Y))

for i in range(len(X)):
   for j in range(len(Y[0])):
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)
