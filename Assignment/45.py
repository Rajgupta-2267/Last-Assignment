#Ques-45: List
lst1=[[1,2],[3,4]]
lst2=[[5,6],[7,8]]
lst3=[]
lst=[]
for i in range(len(lst1)):
    lst4=[]
    for j in range(len(lst1[i])):
        lst4.append((lst[i][j]+lst2[i][j]))
    lst3.append(lst4)
print(lst3)