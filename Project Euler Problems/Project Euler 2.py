# max amount of numbers in sequence terms
nseq = 4000000

# first two terms
n1 = 1
n2 = 2

#Starts the count because 2-1 = 1, keeps track for sequence terms
count = 2


if nseq <= 0:
   print("Integer needs to be positive")
   #Checks if valid number
   
   
elif nseq == 1:
   print("Fibonacci sequence up to",nseq,":")
   print(n1)
   # if nterms = 1 , can only get 0 in sequence
   
   
else:
   print("Fibonacci sequence upto",nseq,":")
   print(n1,",",n2,end=', ')
   while count < nseq:
       nth = n1 + n2
       print(nth,end=' , ')
       # update values, and keeps count of number in sequence
       n1 = n2
       n2 = nth
       count += 1
        #prints all in fib sequence until nseq=count