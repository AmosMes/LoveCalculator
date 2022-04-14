print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_names = name1 + name2
lower_names = combined_names.lower()
list1 = ['t', 'r', 'u', 'e']
list2 = ['l', 'o', 'v', 'e']

first_digit = 0
for i in list1:
  first_digit += combined_names.count(i)

second_digit = 0
for i in list2:
  second_digit += combined_names.count(i)

score = int(str(first_digit) + str(second_digit)) 

if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
