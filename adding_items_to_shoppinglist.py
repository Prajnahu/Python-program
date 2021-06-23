current_choice="_"
computer_parts=[]  #create emtpty list to add item
while current_choice!='0':
    if current_choice in "123456":
        print("adding{}".format(current_choice))
        if current_choice=="1":
            computer_parts.append("computer")
        elif  current_choice=="2":
            computer_parts.append("moniotr")
        elif current_choice=="3":
            computer_parts.append("mouse")
        elif current_choice=="4":
            computer_parts.append("mouse mat")
        elif current_choice=="6":
                computer_parts.append("hdmi")


    else:
        print('please add the options from the lists below')
        print("1.computer")
        print("2.monitor")
        print("3.keyboard")
        print("4.mouse")
        print("5. mouses mat")
        print("6.hdmi calbe")
        print("0.finish")
    current_choice=input()

print(computer_parts)

print('''**********************


''')

avaialbe=["computer","monitor","mouse","mousemat","hdmi"]
current_choice="_"
computer_parts=[]  #create emtpty list to add item
while current_choice!='0':
    if current_choice in "123456":
        print("adding{}".format(current_choice))
        if current_choice=="1":
            computer_parts.append("computer")
        elif  current_choice=="2":
            computer_parts.append("moniotr")
        elif current_choice=="3":
            computer_parts.append("mouse")
        elif current_choice=="4":
            computer_parts.append("mouse mat")
        elif current_choice=="6":
            computer_parts.append("hdmi")


    else:
        print('please add options from the list below:')
        for part in available:
            print("{0}:{1}".format(available.index(part)+1,part))

print(computer_parts)


