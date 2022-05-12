from time import*
import threading

#timer function
print("This FIB finder is on a timer,It takes 10sec to complete")
sleep(2)
user_time = int(input(" how many seconds would you like?: "))
def countdown():
    global my_timer
    my_timer = user_time

    for x in range(user_time):
        my_timer = my_timer -1
        sleep(1)
    print("Out of time")

countdown_thread = threading.Thread(target = countdown)

countdown_thread.start()

#Pause function

while my_timer > 0:
# INTRO
    name =input(" Please enter your NAME to begin: "        )
    print (f"Hi {name}, Welcome to Fibonacci Sequence Finder")
    sleep(2)
    print("is your number a fibonacci?")
# NUMBER FINDER
    fibonacci = [1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597]
    user_input= int(input("Enter number: "))

    if user_input in fibonacci:
        print("yes")
    else: print("not a FIB")
    if my_timer == 0:
                print("press play to go again")
    break