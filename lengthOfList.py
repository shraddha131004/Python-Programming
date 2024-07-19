list = ['ab12','34cd','56fg','98ji'];
#1
print(len(list))
#2
count = 0;
for i in list:
    count+=1
print("length of list",count)
#3
from operator import length_hint
length = length_hint(list)  
print("Length of list is "+str(length))  
    