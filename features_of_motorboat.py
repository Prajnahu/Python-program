bike={"make":"Honda","model":"250 dream","colour":"red"}
#bike={"make":"Honda","model":"250 dream","colour":"red","engine_size":250}
#print(bike["engine_size"])
print(bike["colour"])
k=list(bike.keys())
print(k)
k.sort()
print(k)
for i in k:
    print(i +"-"+bike[i])
print()
print(bike.values())
for j in bike:
    print(bike[j])
print("*"*50)
a=bike.keys()
print(a)
bike["place"]="beach"
print(a)
print("&"*70)
prajna=list(bike.keys())
print(prajna)
prajna.append("world")
print(prajna)
prajna.remove("world")
print(prajna)