#Ques-8: WAP in python to find out whether a number is odd or even using bitwise operator only.
n=int(input("Enter the number to find whether the number is even or odd:\n"))
oe=n&1
if(oe == 1):
    print("The number is odd")
else:
    print("The number is even")