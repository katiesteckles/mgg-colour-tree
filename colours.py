import csv
import string
import sys

with open('/home/pi/Desktop/colours.csv', 'Ur') as f:
#with open('colours.csv', 'r') as f:
    reader = csv.reader(f)
    colours = list(reader)
#print(colours[1:10])
#inputstring = "Check this magenta piece of shit is still working"
inputstring = ""
for j in range(1,len(sys.argv)):
    inputstring += sys.argv[j]
    inputstring += ' '

#print(inputstring)
inputstring_lc = inputstring.lower()
#print(inputstring_lc)
punctuation = set(string.punctuation)
inputstring_np = ''.join(ch for ch in inputstring_lc if ch not in punctuation)
#print(inputstring_np)

for i in range(1,len(colours)):
    if colours[i][0] in inputstring_np:
        #print(inputstring_np)
        #print(colours[i][0])
        print(colours[i][1]),
        break
