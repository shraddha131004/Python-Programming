def ends_with_b(text):
    
    return "Accepted" if q0(text) else "Rejected"
    

def q0(text):
    
    if len(text) == 0:
        return False
    
    if text[0] == 'a':
        return q0(text[1:])
    elif text[0] == 'b':
        return q1(text[1:])
    else:
        return False
        
def q1(text):
    if len(text) == 0:
        return True
    
    if text[0] == 'b':
        return q1(text[1:])
    elif text[0] == 'a':
        return q0(text[1:])
    else:
        return False

print(ends_with_b("babababbababbaba")) 
print(ends_with_b("bbb"))                         
print(ends_with_b("b"))               
print(ends_with_b("a"))
