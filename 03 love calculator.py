print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
combined_names = name1 + name2
combined_names = combined_names.lower()

score_1 = 0
score_2 = 0

score_1 += combined_names.count("t")
score_1 += combined_names.count("r")
score_1 += combined_names.count("u")
score_1 += combined_names.count("e")

score_2 += combined_names.count("l")
score_2 += combined_names.count("o")
score_2 += combined_names.count("v")
score_2 += combined_names.count("e")

total_score = int(str(score_1) + str(score_2))

if total_score < 10 or total_score > 90:
    print(f"Your score is {total_score}, you go together like coke and mentos.")
elif total_score >= 40 and total_score <= 50:
    print(f"Your score is {total_score}, you are alright together.")
else:
    print(f'Your score is {total_score}.')