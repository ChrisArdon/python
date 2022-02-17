#You are going to write a program that adds to a travel_log. You can see a travel_log
#which is a List that contains 2 Dictionaries.

#The inputs for the function are positional arguments. The order is very important.

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country_visited, times_visited, cities_list):
    temp_dictionary = {
        "country": country_visited,
        "visits": times_visited,
        "cities" : cities_list
    }

    travel_log.append(temp_dictionary)
    
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)