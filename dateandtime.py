import time

print(time.gmtime(0))

print(time.localtime()) #creates tuple
#OR
print(time.localtime(time.time()))#same result

print(time.time()) ##number of seconds since start of epoch that jan1 1970

print('-'*50)


#not printing as a tuple in localtime

time_here=time.localtime() #first take the localtime
print(time_here)
#2 ways of printing
print("Years:",time_here[0],time_here.tm_year)
print('*'*50)
print("months:",time_here[1],time_here.tm_mon)
print('*'*50)
print("day:",time_here[2],time_here.tm_mday)
print("Years:",time_here[0])


