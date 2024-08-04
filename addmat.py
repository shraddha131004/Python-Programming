A = [[1,2,3],
     [4,5,6],
     [7,8,9]]
B = [[1,2,3],
     [4,5,6],
     [7,8,9]]
R = [[0,0,0],
     [0,0,0],
     [0,0,0]]
for i in range(len(A)):
    for j in range(len(A[0])):
        R[i][j] = A[i][j] + B[i][j]
        
print(R)