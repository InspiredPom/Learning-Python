import re
#Regex for lastname ([A-Z])[a-z]+$
#https://docs.python.org/2/library/re.html
#http://regexr.com/

string = "Am32423423423anda"
string2 = re.sub('[0-9]', '', string)
print (string2)

if re.match('([A-Z])[a-z]+$', string):
    print(string + 'is a valid last name')
else:
    print(string + ' is not a valid last name')