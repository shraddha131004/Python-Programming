def check_validity(text):
	symbols = {'(',')','{','}','[',']','<','>'}
	pairs = {'(':')','{':'}','[':']','<':'>'}
	res = []
	for symbol in text:
		if symbol in symbols:
			if symbol in pairs:
				res.append(symbol)
			else:
				if res and (pairs[res[-1]] == symbol):
					res.pop()
				
				
				else:
					return False
		
		
		else:
			return False #Invalid text symbols
	if not res :
		return True #valid text
	else:
		return False #Invalid text
		
		
#print(check_validity('((as)}'))

def get_valid_invalid_textCount(mixture):
	strings = []
	valid_count = 0
	invalid_count = 0
	for element in mixture:
		if type(element) is str:
			if check_validity(element):
				valid_count += 1
			else:
				invalid_count += 1
			
		elif type(element) in [list, tuple]:
			
			v_c, inv_c = get_valid_invalid_textCount(element)
			valid_count += v_c
			invalid_count += inv_c
		else:
			pass
	return valid_count, invalid_count
		 
print(get_valid_invalid_textCount(['()',1,'{}','{]',['[]','{}'],('a','[]')]))
