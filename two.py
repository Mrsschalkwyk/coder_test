
print("is your number a fibonacci?")

fibonacci = [1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597]
user_input= int(input("Enter number: "))

if user_input in fibonacci:
    print("yes")
else:
    print("no")
print("click play to try again")
