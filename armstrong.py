num = int(input('Enter any number:'))
orig = num
sum = 0
while(num >0):
	i = num%10
	sum = sum + i**3
	num //= 10
	
if(orig == sum):
	print('Armstrong number.')
else:
	print('Not a Armstrong number.')
