#create a list called even
#create another list called odd
#loop through the values from 1 to 100
#if number is even, add it to even list
#if number is odd, add it to odd list

even = []
odd = []

for i in range(1, 10):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)