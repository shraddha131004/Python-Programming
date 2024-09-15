decimal_dictionary = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}

def decimal_subtraction(num1,num2):

	def str_to_int(text):
		result=0
		text_length=len(text)
		if text_length==0:
			return 0
		elif text_length==1:
			return decimal_dictionary[text]
		else:
			return decimal_dictionary[text[0]]*pow(10,text_length-1)+str_to_int(text[1:])
	
	def borrow_subtract(num1,num2):
		if len(num1) < len(num2):
			num1, num2 = num2, num1
		num2 = num2.zfill(len(num1))
		result = []
		borrow = 0
		
		for i in range(len(num1)-1,-1,-1):
			digit1 = decimal_dictionary[num1[i]]-borrow
			digit2 = decimal_dictionary[num2[i]]
			
			if digit1 < digit2:
				borrow = 1
				digit1 += 10
			else:
				borrow = 0
			
			result_digit = digit1 - digit2
			result.append(str(result_digit))
			
		result=result[::-1]
		return ''.join(result).lstrip('0') or '0'
		
	int_num1 = str_to_int(num1)
	int_num2 = str_to_int(num2)
			
	if int_num1 > int_num2:
		result = borrow_subtract(num1,num2)
	elif int_num1 < int_num2:
		result = '-' + borrow_subtract(num2, num1)
	else:
		result = '0'
		
	return result
	
print(decimal_subtraction("133", "9")) 
print(decimal_subtraction("122", "10"))  
print(decimal_subtraction("123", "15"))  
print(decimal_subtraction("12", "12"))
