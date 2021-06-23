print("lol!welcome to faulty calculator")  ##76 AND 24
a=int(input("enter the no. you want to calculate"))
b=int(input("enter another no. involved in the calculation"))
print('''
1.add
2.sub
3.multiply
4.divide''')
opr=int(input("select the above no."))
if opr==1 and a==76 and b==24:
    print("46")

elif opr==1:
    ans=int(a+b)
    print("ans is {}".format(ans))

elif opr==2 and a==21 and b==5:
    print("02")

elif opr==2:
    ans=int(a-b)
    print("ans is {}".format(ans))
elif opr==3 and a==45 and b==3:
    print("124")
elif opr==3:
    ans=int(a*b)
    print("ans is {}".format(ans))
elif opr==4 and a==49 and b==6:
    print("4")
else:
    ans=int(a/b)
    print("ans is {}".format(ans))
