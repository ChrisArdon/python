#The function is_leap() should return True if it is a leap year and return False if it is not a leap year.
#You are then going to create a function called days_in_month() which will take a year and a month as inputs.
#And it will use this information to work out the number of days in the month, then return that as the output.


def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                #Leap year
                return True
            else:
                #Not Leap Year
                return False
        else:
            #Leap Year
            return True
    else:
        #Not Leap Year
        return False

def days_in_month(i_year, i_month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(i_year):
        #Print the days of february
        if i_month == 2:
            return month_days[i_month -1] + 1
        else:
            return month_days[i_month - 1]        
    else:
        return month_days[i_month - 1]

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)







