"""Ques-2: Swapping with using third variable."""
a=int(input("Enter a number\n"))
b=int(input("Enter another number\n"))
print("Before swapping :\na = %d\nb = %d"%(a,b))
c=a
a=b
b=c
print("After swapping :\na = %d\nb = %d"%(a,b))