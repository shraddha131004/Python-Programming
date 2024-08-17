def capital_case(text):
	res =''
	for char in text:
		if 'a' <= char <= 'z':
			res += chr(ord(char)-32)
		else:
			res += char
	return res
	
def small_case(text):
	res =''
	for char in text:
		if 'A' <= char <= 'Z':
			res += chr(ord(char)+32)
		else:
			res += char
	return res
	
def reverse_case(text):
	res =''
	for char in text:
		if 'a' <= char <= 'z':
			res += chr(ord(char)-32)
		elif 'A' <= char <= 'Z':
			res += chr(ord(char)+32)
			
	return res

def zigzag_case1(text):
	res =''
	for index,char in enumerate(text):
		if index%2 == 0: 
			if 'a' <= char <= 'z':
				res += chr(ord(char)-32)
			else:
				res += char
		else:
			if 'A' <= char <= 'Z':
				res += chr(ord(char)+32)
			else:
				res += char
			
	return res
	
def zigzag_case2(text):
	res =''
	for index,char in enumerate(text):
		if index%2 == 0: 
			if 'A' <= char <= 'Z':
				res += chr(ord(char)+32)
			else:
				res += char
		else:
			if 'a' <= char <= 'z':
				res += chr(ord(char)-32)
			
			else:
				res += char
			
	return res	

def change_case(text,style):	
	if style in ['c','C']:
		return capital_case(text)
		#t = text.replace(text,text.upper())
		#return t
			
	elif style in ['S',"s"]:
		return small_case(text)
		
	elif style in ['R',"r"]:
		return reverse_case(text)
		
	elif style in ['Z','z']:
		return zigzag_case1(text)
		return zigzag_case2(text)
		
	else:
		return "Style not recognized,please enter correct style."

print(change_case('q23',"z"))




