import time


t = int(input("how many seconds do you want to set the time for?"))

while t:
    mins = t // 60
    secs = t % 60
    timer = '{:02d}:{:02d}'.format(mins,secs)
    print(timer,"end") #try without

    t-=1
    print('Lets Begin!')