#Ques-35 Swap using function.
f=lambda x,y:x+y
n=int(input("Enter number of terms : "))
a=0
b=1
print(a,b,end=' ')
for i in range(n-2):
    z=f(a,b)
    a=b
    b=z
    print(z,end=' ')