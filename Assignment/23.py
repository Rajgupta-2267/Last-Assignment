#Ques-23: Form a dictionary from the user.
d={}
for i in range (3):
    x=int(input('Enter Key : '))
    d1={}
    y=int(input('Enter key for nested : '))
    z=int(input('Enter value : '))
    d1.update({y:z})
    p=d1
    d.pdate({x:p})
print(d)