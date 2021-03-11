#create a string
#print three letters at a time

text = "applebanana"
for i in range(0, len(text)-1, 3):
    print(text[i:i+3])