def max(a,b):
    if(a>b):
        return a
    else:
        return b

def min(a,b):
    if(a<b):
        return a
    else:
        return b
a = input("Enter first number")
b = input("Enter second number")
print("Maximum of numbers ",a, "and ", b," is",max(a,b))
print("Minimum of numbers ",a, "and ", b," is",min(a,b))