# https://www.w3schools.com/python/python_datetime.asp
from datetime import datetime


if __name__ == "__main__":
    right_now = datetime.now()
    print(right_now)
    print(right_now.strftime("%A, %d %B, %Y %H:%M:%S %p"))
    # Local versions
    print(right_now.strftime("%x %X"))  # depends on pc settings!

    print(right_now.year)
    print(right_now.month)
    print(right_now.day)
    print(right_now.hour)

    date = datetime(year=1999, month=1, day=11)
    print(date)