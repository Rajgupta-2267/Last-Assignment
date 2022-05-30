#Ques-31: Change the key of nested dictionary.
dict1 = {}
n = int(input("Enter the number of elements you want to store in dictionary : "))
for i in range(n):
    print()
    a = eval(input("Enter key %d : " % (i+1)))
    dict2 = {}
    b = eval(input("Enter nested key %d : " % (i+1)))
    c = eval(input("Enter value : "))
    dict2.update({b: c})
    dict1.update({a: dict2})
print(dict1)
print()
x = eval(input("Enter the nested key you want to change : "))
for i in dict1.values():
    for j in i.keys():
        if x == j:
            y = eval(input("Enter New Key : "))
            i.update({y: i[j]})
            i.pop(j)
            print()
            print("Updated Dictionary :", dict1)
            break