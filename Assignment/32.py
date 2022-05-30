#Ques-32: separate all positive number from the list using lambda function.
ls=[1,-2,3,-4,5,-6]
lst1=list(filter(lambda n:n>0,ls))
print(lst1)