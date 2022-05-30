#Ques-3: Without using third variable and any other variable.
a=int(input("Enter a number\n"))
b=int(input("Enter another number\n"))
print("Before swapping :\na = %d\nb = %d"%(a,b))
a,b=b,a
print("After swapping :\na = %d\nb = %d"%(a,b))
