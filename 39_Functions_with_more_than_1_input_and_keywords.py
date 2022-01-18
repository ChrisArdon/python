#Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")
greet_with("Andrea", "San Salvador")

print("______")

#Functions with keyword arguments
greet_with(name="Gisselle", location="Altavista") #Here the location doesn't matters