number=int(input("eneter the integeer"))
booleanexp=input("enter True or False")
if booleanexp=="true".casefold():
    for i in range(1,number+1):
        print(i*'*')
elif booleanexp=="False".casefold():
    while number!=0:
        print(number*'*')
        number=number-1


