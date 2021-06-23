#Create a program that takes some text and return a list of all the characters in the text
#that are not vowels ,sorted in alphabetical order.
#you can either enter the text from keyboard or initia;lise a string variable with the string

sample_text="python is a very powerful language"
vowels=frozenset("aeiou")
#vowels={"a","e","i","o","u"}
finalset=set(sample_text).difference(vowels)
print(finalset)


finallist=sorted(finalset)
print(finallist)