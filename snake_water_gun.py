import random
computer_choice = random.randint(1,3)
#print(computer_choice) =computers choice is hidden

choose=int(input("enter '1' for snake,'2' for water and '3' for gun"))
print(choose)

if computer_choice==choose:
    print("its a tie")
elif computer_choice==1 and choose==2:
    print("user wins")
elif computer_choice==1 and choose==3:
    print("user wins")
elif computer_choice==2 and choose==1:
    print("computer wins")
elif computer_choice==2 and choose==3:
    print("computer wins")
elif computer_choice==3 and choose==1:
    print("computer wins")
else:
    print("user wins")

