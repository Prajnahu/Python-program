import time
#from time import perf_counter as my_timer
from time import monotonic as my_timer
import random

input("enter to start the game")

wait_time=random.randint(1,6)
time.sleep(wait_time)
start_time=my_timer()
input("press enter to end the game")
end_time=my_timer()

print("start time"+time.strftime("%X",time.localtime(start_time)))
print("end time is"+time.strftime("%X",time.localtime(end_time)))

print("your reactiion time was {} ".format(end_time-start_time))

#the output isnt current time
#perf_counter is precise clock
#montonic =here the time cant go backwards and no adjustment cant be made