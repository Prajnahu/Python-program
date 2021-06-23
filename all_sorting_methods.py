pangram="The quick brown fox jumps over the lazy dog"
letter=sorted(pangram)
print(letter) ##output is in lists in order

numbers=[2.3,9,4,5,6,3,4,8,7,0.1,00.009]
l=sorted(numbers)
print(sorted)


print(''''



''')

numbers.sort()
print(numbers)##the output is sored no duplicate ,it chamges the lists that we call.SORTED doesnt alter the orginial list it creats dupliacte list
print('''


''')
missing_letter=sorted("The quick brown fox jumped over a lazy dog")
print(missing_letter)

print('''




''')
missing_letter=sorted("The quick brown fox jumped over a lazy dog",key=str.casefold) ##no paranthesis used
print(missing_letter)
print('''

''')

names=["Graham",
       "Jhon",
       "terry",
       "eric",
       "Terry",
       "micheal"]
names.sort(key=str.casefold)
print(names)


print('''


''')
                                                      ##CREATE A LIST
empty_list=[]
even=[2,4,6,8]
odd=[1,3,5,7,9]

#by concatination
num=even+odd
print(num)
sorted_numbers=sorted(num)
print(sorted_numbers) ##original remains the same
print(num)

print('''


''')
digits=sorted("432985617")
print(digits)
digit=list("345t28930")
print(digit)
#more_numbers=list(num)
more_numbers=num[:]
print(more_numbers)
print(num)

print(num is more_numbers)
print(num==more_numbers)

##ANOTHER WAY TOP  CREATE A LIST IS BY SLICING
more_numbers=num[:]


##METHOD4 OF CREATING A LIST
more_num=num.copy()
print(more_numbers)
print(num)






