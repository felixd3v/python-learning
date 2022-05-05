from datetime import date
from datetime import time
from datetime import datetime

def main():

    # Get today's date
    today = date.today()
    print("Today is", today)

       # Print individual components of dates
    print("Components of date:", today.day, today.month, today.year)

    # Get date of the week number, e.g. Monday is 0, Sunday is 6
    print("Today's weekday number is", today.weekday())
    
    # Get today's date and time
    today = datetime.now()
    print("The current date and time is", today)

    # Get current time
    currentTime = datetime.time(datetime.now())
    print("The current time is", currentTime)
if __name__ == "__main__":
    main()