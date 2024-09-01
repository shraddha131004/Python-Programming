def sliceOperator(object, start=None, end=None, step=1):
    
    if start is None:
        start = 0
    if end is None:
        end = len(object)
    
    # Handle negative indices
    if start < 0:
        start += len(object)
    if end < 0:
        end += len(object) 
    
    result = []
     
    index = start
    while (step > 0 and index < end) or (step < 0 and index > end):
        result.append(object[index])
        index += step

    return result

print(sliceOperator([1, 2, 3, 4, 5], 1, 4))      
print(sliceOperator("Hello, World!", 7, 12))
