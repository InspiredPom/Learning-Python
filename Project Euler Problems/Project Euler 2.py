n1 = 1
n2 = 1
count = 0
sum = 0
#Declare values
#Numbers 1,2
#count = number currently on
while count < 4000000:
#Limit of 4,000,000
   count = (n1+n2)
   #loop through fibi. numbers = n1 +n2 in sequence
   
   if count%2 == 0:
     #Finds/ Checks if number even
       sum = count + sum
       #Adds to sum of even fib numbers
   n1 = n2
   n2 = count
   #Goes to next numbers in fib sequence
   #print sum of even fib numbers
print (sum)