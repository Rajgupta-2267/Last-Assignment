#Ques-28: Two nested dictionaries, first element of first dict and last element of second dict to add in third dictionary.
dict1 = {}
n = int(input("Enter the number of elements you want to store in dictionary 1 : "))
for i in range(n):
    print()
    a = eval(input("Enter key %d : " % (i+1)))
    dict3 = {}
    b = eval(input("Enter nested key %d : " % (i+1)))
    c = eval(input("Enter value : "))
    dict3.update({b: c})
    dict1.update({a: dict3})
print()
dict2 = {}
m = int(input("Enter the number of elements you want to store in dictionary 2 : "))
for i in range(m):
    print()
    a = eval(input("Enter key %d : " % (i+1)))
    dict3 = {}
    b = eval(input("Enter nested key %d : " % (i+1)))
    c = eval(input("Enter value : "))
    dict3.update({b: c})
    dict2.update({a: dict3})
print()
print("Dictionary 1 = ", dict1)
print("Dictionary 2 = ", dict2)
print()
dict3 = {}
for i in dict1.keys():
    dict3.update({i: dict1[i]})
    break
for i in dict2.keys():
    continue
dict3.update({i: dict2[i]})
print("New Dictionary = ", dict3)