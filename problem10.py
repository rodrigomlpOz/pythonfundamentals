#print numbers from 1 to 100
#if number is divisible by 3, print FIZZ
#if number is divisible by 5, print BUZZ
#if number is divisible by both 3 and 5, print 
#FIZZBUZZ
#else, print the number

for i in range(1, 101):
    if (i % 3 == 0 and i % 5 == 0):
        print("FIZZBUZZ")
    elif (i % 3 == 0):
       print("FIZZ")
    elif (i % 5 == 0):
        print("BUZZ")
    else:
        print(i)