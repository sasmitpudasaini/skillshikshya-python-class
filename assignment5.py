#find leap year

def leap_year(date):
    if (date % 4 == 0 and date % 100 != 0) or (date % 400 == 0):
        return ("the next leap year is ",date)
    else:
        return leap_year(date+1)
print(leap_year(4))


def rec_palindrome(data):
    if (len(data) <= 1):
        return (f"{data} is a palindrome")
    if(data[0] != data[-1]):
        return rec_palindrome(f"{data} is not a palindrome")
    else:
        return (f"{data} is not a palindrome")
print(rec_palindrome("RACECAR"))

