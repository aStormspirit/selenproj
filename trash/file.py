#f = open('users.txt', 'r')
#text = f.read()
#print(text)
import re

o = open('users.txt','a') #open for append
f = open('users2.txt','w')
for line in open('users.txt'):
    line2 = re.sub('/k/','/z/',line)
    f.write(line2)

f.close()
o.close()