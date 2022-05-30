#Ques-25: Count the frequency of each character in a string entered by the user and display it using dictionary.
str1 = input('Enter any string :\n')
lst1 = []
lst2 = []
for i in range(26):
    lst1.append(0)              # for lower Case alphabets
    lst2.append(0)              # for Upper Case alphabets
for i in range(len(str1)):
    for j in range(97, 123, 1): # range for lower case alphabets
        if(ord(str1[i]) == j):
            lst1[j-97] += 1
    for j in range(65, 91, 1):  # range for upper case alphabets
        if(ord(str1[i]) == j):
            lst2[j-65] += 1
dict1 = {}                      # for lower case alphabets
dict2 = {}                      # for upper case alphabets
for i in range(26):
    if(lst1[i] != 0):
        a = chr(i+97)
        b = lst1[i]
        dict1.update({a: b})
    if(lst2[i] != 0):
        a = chr(i+65)
        b = lst2[i]
        dict2.update({a: b})
print('For lower Case Letters :', dict1)
print('For upper Case Letters :', dict2)