Again = True

while Again:
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number to add: "))
    print (str(x) + " plus " + str(y) + "=" + str(x+y))
    #print(x + y)


    if input("Again? ") == "no":
        Again = False