#Ques-44: Enter the list from the user and find the sum of its elements using function:
def listsum(lst):
    l=len(lst)
    s=0
    for i in range(l):
        s=s+lst[i]
    return s
lst=eval(input("Enter the list : "))
listsum(lst)