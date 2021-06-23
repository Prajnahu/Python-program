##DIVIDE THE APPLES:to find the divisor
n=int(input("enter the no of apples harry will have"))
mn=int(input("enter the mininum number"))
mx=int(input("enter the max number"))
for i in range(mn,mx):
    print(i)
    if n%i==0:
        print("its divisible")
    else:
        print(" is not a divisor of ")
