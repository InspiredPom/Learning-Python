import re
#Regex for lastname ([A-Z])[a-z]+$
#https://docs.python.org/2/library/re.html
#http://regexr.com/

string = "Am32423423423anda"
string = re.sub('[0-9]', '', string)
print (string)