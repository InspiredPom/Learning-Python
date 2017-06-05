import math

mystring = "New York"
print(mystring.count('N'))

mystring2 = 'the quick brown fox'
print('goose' in mystring2)

mylist = ['whiskey', 'tango','foxtrot']
mylist.sort()
print(mylist)

mystring3 = "Truly, Madly, Deeply"
print(mystring3[2])
print(mystring3[7:12])

print("The value of pie is about %.10f" % math.pi)



x= 'x'
y= 'x**2'
z= 'x**x'
print(x,y.rjust(4) , z.rjust(6))
print ("="*14)
for n in range (1,6):
  nn = str(n**2)
  nnn = str(n**n)
  print (n,nn.rjust(4),nnn.rjust(6))
  print("\n")
  #rjust: right justifies the string within the area
  
  
mylist = [8,33,29,4,1,5,98]
mylist.sort()
print(mylist)
print(len(mylist))
print("numbers in this list\n")
print("\n")
print ([1,2,3] + [4,5,2])
print("\n")
myboo = ("BOO!")
print (list(myboo))

basket = ['apple', 'orange', 'banana']
basket.append('apple')
print(basket)

print("There are  ", basket.count('apple'), "apples")

L= ['spam', 'eggs', 'chicken']
L.append('green eggs')
print(L)
print("\n")

L= ['cookies','milk','candy']
L2= []
for i in L:
  if i is not None:
    L2.append(i)
    print(L2)