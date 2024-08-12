n = int(input())
for i in range(n):
    for j in range(i,n):
        print('*',end = ' ')
    print()
    
for i in range(1,n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print("*",end = ' ')
    print()
 
print()   

for i in range(1,n):
    for j in range(i):
        print(" ",end="")
    for j in range(i,n):
        print("*",end =  '' )
    print()
print()

for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        
        
            print("*",end = ' ')
        
    for j in range(i+1):
        if(i ==1 and j==2):
            print("1",end = ' ')
        else:
            print("*",end = ' ')
    print()       