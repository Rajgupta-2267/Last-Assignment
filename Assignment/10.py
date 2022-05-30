#Ques-10: WAP in python to enter height and base from the user and find the hypotenuse.
b=float(input("Enter the base length of the triangle:\n"))
h=float(input("Enter the height of the triangle:\n"))
print("Hypotenuse of triangle = %.2f"%((b**2)+(h**2))**(1/2))