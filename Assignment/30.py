#Ques-30: Create a dictionary whose is perfect number and value is a strong number in a trange given by the user.
dict1={}
lst1=[]
lst2=[]
print("Enter the range :")
n=int(input("Enter starting value : "))
m=int(input("Enter ending value : "))
for i in range(n,m,1):
    s=0
    for j in range(0,i-1,1):
        if(i%(j+1)==0):
            s=s+j+1
    if(s==i):
        lst1.append(i)
    s=0
    c=i
    while c>0:
        x=c%10
        p=1
        for j in range(1,(x+1),1):
            p=p*j
        s=s+p
        c=c//10
    if(s==i):
        lst2.append(i)
len1=min(len(lst1),len(lst2))
for i in range(len1):
    dict1.update({lst1[i]:lst2[i]})
print(dict1)

