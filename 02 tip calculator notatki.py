two_digit_number = input()
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇
# wariant 1
a = int(two_digit_number[0])
b = int(two_digit_number[1])
print(a + b)

# wariant 2
c = a + b
print(c)

bmi
# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
bmi = int(weight) / float(height) ** 2
bmi_int = int(bmi)
print(bmi_int)

# dzielenie
# zaokrąglenie
round(8 / 3, 2)
# wynik jako int, nie float
8 // 3

# f-string
score = 0
height = 1.8
isWinning = True
print(f"Your score is {score}, heigh is {height}, is {isWinning}")

# time left on earth
age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

age = int(age)
weeks = age * 52
all = 90 * 52
left = all - weeks
print(f"You have {left} weeks left.")


# procent z liczby
suma = 60
procent = 10
wynik = int(suma * (procent / 100))
print(f"{wynik}")

# procent dodany do liczby
suma = 60
procent = 10
dodane = int(suma * (1 + (procent / 100)))
print(f"{dodane}")

# formatowanie zaokrąglenia
var_2places = "{:.2f}".format(var)