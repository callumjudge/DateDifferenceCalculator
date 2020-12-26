from time import sleep

print("Welcome to the Date Calculator - Please Follow the Instructions:")

sleep(2)
print("The format we will be using will be DD/MM/YYYY")

while True:
    try:
        year = int(input("Please input a year of your choice eg 2020: "))
    except ValueError:
        print ("This is not a Valid Year, try again.")
        continue
    else:
        print("Loading......")
        break

sleep(2)

while True:
    try:
        month = int(input("Please input the number of the month you would like: "))
    except ValueError:
        print ("This is incorrect please try again. ")
        continue
    if month in range (1, 13):
        print("Loading.......")
        print(" ")
        break
    else:
        print("This is not a valid month.")
        continue


sleep(1)

while True:
    try:
        day = int(input("Please input a number for your day: "))
    except ValueError:
        print ("This is not a valid day, please try again.")
        continue
    if (month == 1 or 3, 5, 7, 8, 10, 12 and day <= 31)\
            or (month == 2 and day <= 28) \
            or (month == 4, 6, 9, 11 and day <= 30):
        print ("Loading.....")
        break
    else:
        print ("This is not a valid day")
        continue


print ("The first date you have selected is:",day, "/",month, "/",year )






