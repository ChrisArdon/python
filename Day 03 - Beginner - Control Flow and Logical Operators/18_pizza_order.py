# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ") #Small $15, Medium $20, Large $25
add_pepperoni = input("Do you want pepperoni? Y or N ") #For Small +$2, for Medium and Large +$3
extra_cheese = input("Do you want extra cheese? Y or N ") #For all pizzas +$1
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill =+ 25
    
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill =+3
        
if extra_cheese == "Y":
    bill += 1
    
print(f"Your final bill is: ${bill}.")