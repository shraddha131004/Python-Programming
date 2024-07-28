def findHCF(x,y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1,smaller+1):
        if((x%i == 0) and (y%i == 0)):
            hcf = i
    return hcf
    

x = int(input("Enter first number to find hcf:"))
y = int(input("Enter second number to find hcf:"))
print(f"The hcf of {x} and {y} is {findHCF(x,y)}.")
        
        
            
            