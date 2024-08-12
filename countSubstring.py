def count(string,substring,sign):
    if sign == False:
        non_overlapping = string.count(substring)
        return non_overlapping
    else :
        count = start = 0
        for i in range(len(string) - 1):
        
           if string[i] == string[i+1]:
                count+=1
        return count
        
def countSub(string,substring,sign):
	if sign == False:
	  count = start = 0
    
    	while True:
        	   start = s.find(sub, start)
        
        	   if start == -1:
            	     break
                   count += 1
        	   start += len(sub)
    	return count
     
        else:   
        count = start = 0
        while True:
           start = string.find(substring, start) + 1
           if start > 0:
             count += 1
           else:
             break
        return count
        

      


    
print(count("sggggsggsgsgsgggsggs","gg",True))
print(countSub("sggggsggsgsgsgggsggs","gg",False))

