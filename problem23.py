#create a list
#add values 1 + 3 + 5 .. 99 to list
#loop through the list and add all numbers inside of it

x = []
for i in range(1, 100, 2):
    x.append(i)

sum = 0
for val in x:
    sum += val
print(sum)