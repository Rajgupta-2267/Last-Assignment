#Ques-29: Multiply all the elements of the tuple which are stored in dictionary as its value.
dict1 = {}
n = int(input("Enter the number of elements you want to store in dictionary : "))
for i in range(n):
    print()
    a = eval(input("Enter key %d : " % (i+1)))
    dict2 = {}
    m = int(input("Enter the number of elements you want to insert in tuple : "))
    tpl = ()
    for j in range(m):
        b = eval(input("Enter element %d : " % (j+1)))
        tpl += b,
    dict1.update({a: tpl})
print()
print("Dictionary = ", dict1)
print()
c = 0
for i in dict1.values():
    c += 1
    p = 1
    for j in range(len(i)):
        p = p*i[j]
    print("Product of elements in tuple %d = %d" % (c, p))