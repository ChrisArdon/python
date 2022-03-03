# Debugging Odd or Even

number = int(input("Which number do you want to check?"))

if number % 2 = 0:  # Here the problem is the operator.
    print("This is an even number.")
else:
    print("This is an odd number.")


# Debugging Leap Year

# The input is taken as a string.
year = input("Which year do you want to check?")

if year % 4 == 0:  # The error here is that we can operate mathematically with strings.
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")


# Debugging FizzBuzz

for number in range(1, 101):
    # It should be AND, because it is FizzBuzz when the number is divisible by both.
    if number % 3 == 0 or number % 5 == 0:
        print("FizzBuzz")
    # they are not ELIF statements
    if number % 3 == 0:
        print("Fizz")
    if number % 5 == 0:
        print("Buzz")
    else:
        print([number])
