"""Ques-1: Heads and tales."""
h=int(input("Enter the number of heads\n"))
l=int(input("Enter the number of legs\n"))
r=(l/2)-h
c=(2*h)-(l/2)
print("Number of Chickens = %d\nNumber of Rabbits = %d"%(c,r))