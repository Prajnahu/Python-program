def palindrome(string):
    backwards=string[::-1].casefold()
    return backwards==string.casefold() #returns true or false
    return palindrome(string)


word=input("please enter a word to check")
if palindrome(word):
    print("{} is a paliendrome".format(word))
else:
    print("{} is not a paliendrome".format(word))

print()
print()
print()


# def alphanumeric(choice):
#     string=""
#     for char in choice:
#         if char.isalnum():
#             string+=char ##string contains only letters and digits
#
#     print(string)
#     return string[::-1].casefold()==string.casefold()
#
#
# sentence=input("enter the sentence")
# if alphanumeric(sentence):
#     print("its a plaiendrome")
# else:
#     print("mot a palienddrome")




