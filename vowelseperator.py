p=input("enter the word")
p.casefold()
count=0
for j in p:
    if j =='a' or j=='e' or j=='i'or j=='o'or j=='u':
        count=count+1
print(count)