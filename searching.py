shoppinglist=['milk','pasta','eggs','spam','rice']
itemtofind='albestross'
foundat=None   ##initially=0(NULL)

for index in range(len(shoppinglist)):
    if shoppinglist[index]==itemtofind:
        foundat=index
        break
if foundat is not None:
    print('item found at {}'.format(foundat))
else:
    print("{} not found".format(itemtofind))


print('*'*800)

       ##########          OR
shoppinglist=['milk','pasta','eggs','spam','rice']
itemtofind='spam'
foundat=None   ##initially=0(NULL)
if itemtofind in shoppinglist:
    foundat=shoppinglist.index(itemtofind)

if foundat is not None:
    print('item found at {}'.format(foundat))
else:
    print("{} not found".format(itemtofind))