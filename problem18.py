#create a long string
#print two letters at a time, without overlapping letters
text = "applefab"
for i in range(0, len(text)-1, 2):
    print(text[i:i+2])
