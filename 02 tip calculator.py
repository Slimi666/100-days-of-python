print("Welcome to the tip calculator")
bill = float(input("What was a total bill? $"))
percantage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill " ))

# long version:
# tip = bill * (percantage / 100)
# bill_tip = bill + tip
# sum = round(bill_tip / people, 2)

# short version
total = bill * (1 + (percantage / 100))
sum = round(total / people, 2)
sum_pretty = "{:.2f}".format(sum)
print(f"Each person should pay ${sum_pretty}")