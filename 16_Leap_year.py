# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#Es bisiesto si es divisible entre 4.
#Pero no es bisiesto si es divisible entre 100.
#Pero si es bisiesto si es divisible entre 400

#2000 y 2400 si son bisiestos son divisibles entre 100 pero tambien entre 400.
#1900, 2100, 2200 y 2300 no lo son porque solo son divisibles entre 100).

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('Leap year.')
        else:
            print('Not leap year.')
    else:
        print('Leap year.')        
else:
    print('Not leap year.')
