#Ques-42: Operations between arguments in function:
def cal(num,num1):
    a=num+num1
    b=num-num1
    c=num*num1
    d=num**num1
    e=num/num1
    f=num//num1
    return a,b,c,d,e,f # returns in the form of tuple
x=eval(input())
y=eval(input())
n1,n2,n3,n4,n5,n6=cal(x,y)
print(n1)
print(n2)
print(n3)
print(n4)
print(n5)
print(n6)