#Ques-24: Enter the dict from the user and find the sum of vaules.
d={}
lst=[]
s=0
n=int(input("Enter the number of elements to store in the dictionary : "))
for i in range (n):
    x=int(input("Enter the key : "))
    y=int(input("Enter the value : "))
    s=s+y
    lst.append(y)
    d.update({x:y})
print(d)
print("Sum = ",s)