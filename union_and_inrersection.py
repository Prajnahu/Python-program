even=set(range(0,40,2))
print(len(even))

sqaures_tuple = (4,6,9,16,25)
squares=set(sqaures_tuple)
print(squares)
print(len(squares))

#UNION COMMAND
print(even.union(squares))
print(len(even.union(squares))) #new set has 22 no. its combines the two sets

print(squares.union(even))#same output

#intersection of sets:OUTPUT will the common item of both the list
print("-"*40)
print(even.intersection(squares))
print(even&squares)
print(squares.intersection(even))
print(squares&even)
print()
print()
#TO SORt and
#TO SUBTRACT A SET:So subtracting set b from set a removes any item that exists in set b from set a
even=set(range(0,40,2))
print(len(even))

sqaures_tuple = (4,6,9,16,25)
print(sorted(even)) # sort converts to list
squares=set(sqaures_tuple)
print(sorted(squares))
print()
print("even minus squares")
print(squares.difference(even))
print(squares-even)
print(even.difference(squares))
print(even-squares)

#Now, there's also an update difference method and that performs the subtraction in place.In other words, it doesn't return a new set, but what it does it modifies the set upon which it is called on.












print('*'*40)
print(sorted(even))
print(squares)
even.difference_update(squares)
print(sorted(even))

#SYMMETRIC DIFFERENCE Of TWO SETS:symmetric difference of two sets, so What that is a symmetric difference of two sets is all the members that are in one set or the other but not both.
#OR opposite of intersection
#we can use up arrow symbol
sqaures_tuple = (4,6,9,16,25)
print(sorted(even))
squares=set(sqaures_tuple)
print(sorted(squares))
print("symmetric even minus squares")
print(sorted(even.symmetric_difference(squares)))

print("symmetric squares minus even")
print((squares.symmetric_difference(even)))



#REMOVE OR DISCARD ITEM FROM SETS
#REMOVES GIVES AN ERROR WHN THAT ITEM ISNT IN THAT SET
print('+'*40)
squares.discard(4)
squares.remove(16)
squares.discard(8)
print(squares)
#squares.remove(8) :OUTPUT:error
#to safely use remove use if condition to check
if 8 in squares:
    squares.remove(8) #NO error but no acction taken
print()
#to trip an error if remove is used and that item isnt in that set

try:
    squares.remove(8)
except KeyError:
    print("the item isnt a memeber of the set")

#TO ACCESS IEM FROM SETS USE GET
#[] get(); for dictionary
#SUBSET OR SUPERSET
print()
print()
print('$'*40)
even=set(range(0,40,2))
print(even)
sqaures_tuple = (4,6,9,16,25)
squares=set(sqaures_tuple)
print(squares)
if squares.issubset(even):
    print("square is a subset of even")


if even.issuperset(squares):
    print("even is a superset of squares")

#NOTES
#FROZEN SET:ITS AN IMMUTABLE SET,cant be changes it can used a dictionary key and also add frozen set as a memeber of a set
#no add,no dicard
#to use frozen set pass one as parameter to a different underscore update core on a regular set.
even=frozenset(range(0,100,2))
print(even)
#print(even.add(3)): error as they are immutable