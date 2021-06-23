ans=5

print("please guess a no btw 1 and 10:")
guess=int(input())

if guess<ans:
    print('guess higher no.')
    guess =int(input('guess another no'))

    if guess==ans:
        print("you win")
    else:
        print('wrong again')

elif guess>ans:
    print("please guess lower")
    guess =int(input('guess another no'))

    if guess==ans:
        print("you win")
    else:
        print('wrong again')
else:
    print('you got it first time')


 ##priotiry is as follows:
 ##if->elif->else
