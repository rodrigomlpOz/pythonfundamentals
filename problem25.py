#create an integer
#count the number of digits

num = 231231231
counter = 0

while num > 0:
    num = num // 10
    counter += 1
print(counter)