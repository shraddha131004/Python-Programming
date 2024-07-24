num = int(input('Enter a number:'))
i = num
revnum = 0
while(num>0):
	revnum = revnum*10 + (num%10)
	num //= 10
	
if(i == revnum):
	print("Is a Palindrome.")
else:
	print("Not a Palindrome.")
	
	
