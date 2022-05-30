#Ques-21: Apples in 7-7 groups no apple left.
a=int(input("Enter the number of apples\n"))
if ( a%7==0 and a%6==1 and a%5==1 and a%4==1 and a%3==1) :
    print("Valid")
else :
    print("Invalid")