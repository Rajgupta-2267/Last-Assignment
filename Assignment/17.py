#Ques-17: Input all angles of triangle and check whether the triangle can be formed or not.
a=int(input("Enter first angle\n"))
b=int(input("Enter second angle\n"))
c=int(input("Enter third angle\n"))
if (a+b+c == 180) :
    print("Triangle can be formed with the given parameters")
else :
    print("Triangle cannot be formed with the given parameters")