def baseChangeFunc(text, text_base, output_base):
    digitsAndAlpha = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    if not (2 <= text_base <= 36) and (2 <= output_base <= 36):
        print('Give base between 2 to 36.')

    decimal_value = int(text, text_base)

    while decimal_value > 0:
        rem = decimal_value % output_base
        result = digitsAndAlpha[rem] + result
        decimal_value //= output_base

    return result


print(baseChangeFunc('100', 2, 8))
print(baseChangeFunc('23', 4, 10))        
print(baseChangeFunc('1010', 2, 16))        
print(baseChangeFunc('1F', 16, 2))        
print(baseChangeFunc('123', 4, 10))         
print(baseChangeFunc('Z', 36, 10))          

