print("Welcome to the rollercoaster!")
bill = 0
height = int(input("What is Your height in cm? "))
if height >= 120:
    print("You can ride rollercoaster!")
    age = int(input("What is Your age? "))
    if age < 12:
        print("Child tickets are $5")
        bill = 5
    elif age <= 18:
        print("Youth tickets are $7")
        bill = 7
    elif age >= 45 and age <= 55:
        print("Midlife crisis is okey, you can ride for free")
    else:
        print("Adults pay $12")
        bill = 12

    photos = input("Do you want a photo for $3? Y or N. ")
    if photos == "Y":
        bill += 3
    elif photos == "y":
        bill += 3

    print(f"Your total bill is ${bill}")
else:
    print("Sorry, You have to grow taller before You can ride.")