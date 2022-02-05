num_char = len(input("What is your name?"))

print(type(num_char))#It gives us the type of the variable

#We need to convert the num_char variable to string, in order to concatenate

new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")