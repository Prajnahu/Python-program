available_exits=['north','south','east','west']

chosen_exit=""
while chosen_exit not in available_exits:
    chosen_exit=input('please choose a direction: ')
    if chosen_exit.casefold()== "quit":
        print('game over')
        break

print('arent you glad you are out of there')

for i in range(0, 100, 7):
    print(i)
    if i > 0 and i % 11 == 0:
        break


for x in range(21):
    if x % 3 == 0 or x % 5 == 0:
        continue
    print(x)
