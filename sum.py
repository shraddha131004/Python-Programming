n = int(input('Enter n:'))
def sumOfNubers(n):
    s = int(sum(range(0,(n+n%2))))
    print('Sum of',n,'natural numbers is',s)

def sumOfSquare(n):
    sum = 0
    for i in range(0,(n+n%2)):
        sum = sum+(i**2)
    print("Sum of square of",n,'natural numbers is',sum)
    
def sumOfCube(n):
    sum = 0
    for i in range(0,(n+n%2)):
        sum = sum+(i**3)
    print("Sum of square of",n,'natural numbers is',sum)
    
    
sumOfNubers(n)
sumOfSquare(n)
sumOfCube(n)
