def modulo(num,deno):
    quotient = int(num/deno)
    remainder = num - (deno * quotient)
    return remainder
    
def moduloWithDivmod(num,deno):
	quotient , remainder = divmod(num,deno)
	return remainder

print(modulo(8.9,3))
print(moduloWithDivmod(8.9,3))
