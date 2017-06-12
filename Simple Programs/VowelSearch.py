mystring = input ("Please enter a string: \n")
vowels = set ("aeiou")
mystring = mystring.lower()
for a in mystring:
	if a in vowels:
		print(mystring, "has a vowel")
		break
else:
		print(mystring, "does not have a vowel")