#Ques-18: Calculate the profit and loss percentage where the selling price and cost price is given by the user.
cp=float(input("Enter the cost price of the product\n"))
sp=float(input("Enter the selling price of the product\n"))
gain = sp-cp
if (gain > 0) :
    print("Gain percentage = %.2f%%"%((gain/cp)*100))
elif (gain < 0) :
    print("Loss percentage = %.2f%%"%((-gain/cp)*100))
elif (gain == 0) :
    print("No profit and No Loss")