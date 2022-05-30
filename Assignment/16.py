#Ques-16: Input all sides of triangle and check whether the triangle can be formed or not.
a=int(input("Enter first side\n"))
b=int(input("Enter second side\n"))
c=int(input("Enter third side\n"))
if ((a+b) > c and (b+c) > a and (c+a) >b) :
    print("Triangle can be formed with the given parameters")
else :
    print("Triangle cannot be formed with the given parameters")