# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1_lower = name1.lower()
name2_lower = name2.lower()

T_count = name1_lower.count("t") + name2_lower.count("t")
R_count = name1_lower.count("r") + name2_lower.count("r")
U_count = name1_lower.count("u") + name2_lower.count("u")
E_count = name1_lower.count("e") + name2_lower.count("e")

L_count = name1_lower.count("l") + name2_lower.count("l")
O_count = name1_lower.count("o") + name2_lower.count("o")
V_count = name1_lower.count("v") + name2_lower.count("v")
E_count = name1_lower.count("e") + name2_lower.count("e")

true_count = T_count + R_count + U_count + E_count
love_count = L_count + O_count + V_count + E_count
score = str(true_count) + str(love_count)

if int(score) <= 10 or int(score)  > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif int(score)  >= 40 and int(score) <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")