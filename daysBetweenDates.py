days_in_months_regular = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_in_months_leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap_year(year):
    """helper function that returns True if 
    year is a leap year """
    if year % 4 == 0:
        return True
    return False


# is_leap_year tests
# print(is_leap_year(2000)) # True
# print(is_leap_year(2002)) # False
# print(is_leap_year(2008)) # True
# print(is_leap_year(2019)) # False
# print(is_leap_year(2020)) # True

def days_in_month(year, month):
    """helper function that receives a year and month,
    and returns the number of days in that month, taking
    differing month lenghts and leap years into account """
    if is_leap_year(year):
        return days_in_months_leap_year[month - 1]
    return days_in_months_regular[month - 1]


# days_in_month tests
# print(days_in_month(2000, 2)) # 29
# print(days_in_month(2001, 2)) # 28
# print(days_in_month(2020, 4)) # 30
# print(days_in_month(2020, 7)) # 31


def next_day(year, month, day):
    """helper function that takes a valid date and 
    returns the date of the following day. """
    if day < days_in_month(year, month):
        return year, month, day + 1
    elif day == days_in_month(year, month) and month < 12:
        return year, month + 1, 1
    elif day == days_in_month(year, month) and month == 12:
        return year + 1, 1, 1


# next_day tests
# print(next_day(1999, 12, 30))  # 1999, 12, 31
# print(next_day(1999, 12, 31))  # 2000, 1, 1
# print(next_day(2000, 6, 30))  # 2000, 7, 1
# print(next_day(2000, 4, 9))  # 2000, 4, 10


def days_between_dates(y1, m1, d1, y2, m2, d2):
    days = 0

    while (y1, m1, d1) != (y2, m2, d2):
        days += 1
        y1, m1, d1 = next_day(y1, m1, d1)

    return days


# days_between)_dates tests
# print(days_between_dates(2020, 8, 30, 2020, 9, 1)) # 2
# print(days_between_dates(2020, 2, 4, 2020, 3, 4)) # 29
# print(days_between_dates(2012, 1, 1, 2012, 1, 2)) # 1
# print(days_between_dates(1920, 8, 30, 2020, 9, 1)) # ?
