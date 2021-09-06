choice=int(input("Enter Number of choice from these \n 1.Sum/2.Subtract/3.Multiply/4.Divide/ :"))
a=int(input("Enter !st Number "))
b=int(input("Enter 2nd Number "))


if choice==1:
    print(a+b)  #Addition

elif choice==2:
    print(a-b)  #Subtraction

elif choice==3:
    print(a*b)  #Multiply

elif choice==4:
    print(a/b)  #Divdie

else:
    print('Invalid Choice')