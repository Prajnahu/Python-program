LOW= 1
HIGH= 1000
# print("please think of a no. btw {} and {}".format(low, high))
# input("press enter to start")
def guess_binary(answer, low, high):
    guesses = 1
    while True:
    # print("\t guessing in the range of {} to {}".format(low,high))
        guess = low + (high - low) // 2
    # high_low = input("my guess is {}.should i guess high or lower ?"
    #                  "type l,h,c for correct ?"
    #                  .format(guess)).casefold()


    # if high_low=="h" :
        #guess higher the low end of the range becomes 1greater than the guesss
        if guess<answer:
            low=guess+1
    #elif high_low=="l":
        elif guess>answer:
            high=guess-1
        #guess lower:the higher end og the rage becomes one less than the guess
    # elif high_low=="c":
        elif guess==answer:
       # print("i got the no. in {}".format(guesses))
        #break
            return guesses

    # else:
    #     print("please enter h,l or c") ##remind the three options

    guesses=guesses+1


for number in range(LOW,HIGH+1):
    number_of_guesses=guess_binary(number,low,high)
    print("{} guessed in {}".format(number,number_of_guesses))