#Ques-20: Salary.
bs=float(input("Enter the base salary of the employee\n"))
if (bs <= 10000) :
    print("Total Salary = %.2f"%(bs+(20/100)*bs+(80/100)*bs))
elif (bs > 10000 and bs <= 20000) :
   print("Total Salary = %.2f"%(bs+(25/100)*bs+(85/100)*bs))
else :
    print("Total Salary = %.2f"%(bs+(30/100)*bs+(95/100)*bs))