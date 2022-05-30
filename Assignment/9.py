#Ques-9: WAP in python to enter two coordinates by the user and find the distance between the coordinates.
x1=float(input("Enter the value of x1:\n"))
y1=float(input("Enter the value of y1:\n"))
x2=float(input("Enter the value of x2:\n"))
y2=float(input("Enter the value of y2:\n"))
x3=(x2-x1)**2
y3=(y2-y1)**2
print("Distance between the coordinates is %f"%((x3+y3)**(1/2)))