# Age Calculator
from datetime import datetime, timedelta


def calculate_age(date_input):
    """str date input, calculates the difference in now and that time,
    returns an int"""
    now = datetime.now()
    data = date_input.split("-")
    # Turn given date into a datetime
    year = int(data[2])
    months = int(data[1])
    days = int(data[0])
    given_date = datetime(year, months, days)
    return now.year - given_date.year


print(calculate_age(input("Enter your date (DD-MM-YY): ")))
