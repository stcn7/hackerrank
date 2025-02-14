""" Hackerrank > Python > Intorduction > Write a Function
"""

def is_leap(year):
    #Math funcion for knowing is a year is a leap year. Returning Leap = True or False
    leap = False

    if (year % 400) == 0:
        leap = True
    elif (year % 100) == 0:
        leap = False
    elif (year % 4) == 0:
        leap = True
    else:
        leap = False

    return leap

print(is_leap(1888))
