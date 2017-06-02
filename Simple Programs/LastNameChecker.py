import re
#Regex for lastname ([A-Z])[a-z]+$
#https://docs.python.org/2/library/re.html
#http://regexr.com/

inputLastName = input('Please enter a last name for validation: ')
resultLastName = re.sub('[0-9]', '', inputLastName)
print ('Edited last name: ' + resultLastName)

if re.match('([A-Z])[a-z]+$', inputLastName):
    print(inputLastName + ' is a valid last name')
else:
    print(inputLastName + ' is not a valid last name')

if re.match('([A-Z])[a-z]+$', resultLastName):
    print(resultLastName + ' is a valid last name')
else:
    print(resultLastName + ' is not a valid last name')