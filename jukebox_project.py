# for index,character in enumerate("abcdefghi"):
#     print(index,character)
for t in enumerate("abcdefghi"):
    index,character=t#unppacking
    print(t)    #each tuple takes the value of index and the element

index,character=(0,'a')
print(index)
print(character)

print('''


''')

welcome=("Welcome to my nightmare","Alice cooper",1975)
bad=("Bad comapny","Bad company",1947)
budgie=("Nightflight","budgie",1981)
melda=("More Mayhem","Emilda May",2011)
metallica="Ride the lightining","Metallica",1984
title,artist,year=metallica
print(title)
print(artist)
print(year)
print('''
 
 
 
 ''')

table=("Coffee table",200,100,250,34.70)
print(table[1]*table[2]) #to calculate using tuple

##or unpack to make is simpler

name,length,width,height,price=table #unpack the tuple into different variables
print(length*width)


print('''


''')
#tuple inside a list
albums=[("Welcome to my nightmare","Alice cooper",1975),
        ("Bad company","Bad company",1947),
        ("Nightflight","budgie",1981),
        ("More Mayhem","Emilda May",2011),
        ("Ride the lightining","Metallica",1984),]
print(len(albums))
# print(len(albums))
# for index,p in enumerate(albums):
#     print(index,p)
for i in albums:
    print("album:{},artist:{},year:{}".format(i[0],i[1],i[2]))

print('''


''')

for x in albums:
    name,artist,year=x[0],x[1],x[2]
    print("album:{},artist:{},year:{}".format(name,artist,year))
