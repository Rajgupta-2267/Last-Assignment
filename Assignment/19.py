#Ques-19: Check whether the input number is divisible by both 5 and 11 or not.
a=int(input("Enter the number\n"))
if ( a%5 == 0 and a%11 == 0) :
    print("This number is divisible by both 5 and 11")
else :
    print("This number is not divisible by both 5 and 11")