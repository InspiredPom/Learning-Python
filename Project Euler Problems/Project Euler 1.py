Ans = 0
# Starts at 0
for i in range(0, 1000):
  #counts from 0-1000
     if (i%3==0) or (i%5==0):
       # if divisible by 3 or 5 with 0 remainder adds one
          Ans += i
          #loops through numbers until range is met.
          #print (i)
print ("The sum of all natural multiples (remainder method) of 3 and 5 between 0 and 1000 is " + str(Ans) + ".")