name =input('please enter your name')
age=int(input('how old are you {0}?'.format(name)))
print(age)

if age<18:
    print("you are not allowed to vote,please come back after {0:4} years".format(18-age))

elif age==900:
    print("sorry ,yoda,you died in return of jedi")

else:
    print('you are allowed to vote')
    print("please put an X in the box")
















