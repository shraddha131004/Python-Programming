list = [1,9,6,4,5]

list.sort()
print(list)

temp = min(list)
list[0] = max(list)
list[4] = temp

print(list)
