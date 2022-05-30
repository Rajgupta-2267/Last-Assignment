#Ques-47: Write a program to display the name of all employees whose salary is more than 25000 using nested dictionary.
n = int(input("Enter the number of employees :\n"))
dict1 = {}
for i in range(n):
    a = i+1
    dict2 = {}
    b = input('Enter the name of employee %d : ' % (i+1))
    c = eval(input('Enter salary : '))
    print()
    dict2.update({b: c})
    dict1.update({a: dict2})
print("For all employees :",dict1)
print()
for i in range(n):
    for j in dict1[i+1].values():
        if j<=25000:
            dict1.pop(i+1)
print("For salary more than 25000 :",dict1)