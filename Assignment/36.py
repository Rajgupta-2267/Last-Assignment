#Ques-36: Use of reduce function.
import functools
ls=[1,2,3,4,5,6,7,8,9,10]
print(functools.reduce(lambda a,b:a+b,ls))