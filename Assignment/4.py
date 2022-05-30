#Ques-4: Swapping With using bitwise operator.
a=int(input("Enter a number\n"))
b=int(input("Enter another number\n"))
print("Before swapping :\na = %d\nb = %d"%(a,b))
a=a^b
b=a^b
a=a^b
print("After swapping :\na = %d\nb = %d"%(a,b))