#ADVENTURE GAME WITH MAPS
locations={0:"You are sitting infront of the computer learning python",
           1:"You are standing at the end of the road before a small brick building",
           2:"You are at the top of the hill",
           3:"You are inside a building,a well house for a small stream",
           4:"You are in a valley beside a stream",
           5:"You are in a forest"}
 #WITH RESPECT TO EACH PLACE
exits=[{"Q":0},
        {"W":2,"E":3,"N":5,"S":4,"Q":0},##ROAD
        {"N":5,"Q":0},#hill
        {"W":1,"Q":0},#building
        {"N":1,"W":2,"Q":0},#valley
        {"W":2,"S":1,"Q":0}] ###lists of dictionary
#each index is a location on the map
loc=1#location strts wwith 1
while True:
    available_exits=""
    for direction in exits[loc].keys(): #starting with location 1
        available_exits+=direction+","
    print(available_exits+"hey")

    print(locations[loc])#WHAT THE LOCATON IS

    if loc==0:
        break
    direction=input("availble exsts are"+available_exits.upper())
    print()
    if direction in exits[loc]:
        loc=exits[loc][direction]  ##we use key to retrieve next location
    else:
        print("you cannot go in that direction")



