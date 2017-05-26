num = 13195  
count = 2  
while count * count < num:  
     while num % count == 0:
         num = num / count
		 #This shows it can no further be divided into a smaller factor
     count = count + 1
#Run again until  num =+ the number looking we're looking for.	 
print(num)  
#prints num, which is now the largest factor of the original number we were looking for.
