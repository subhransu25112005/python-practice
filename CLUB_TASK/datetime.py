#Q11
from datetime import datetime

# Today's date
today = datetime.today()
print("Today's date:", today.date())

# Year, Month, Day
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)

# Current time in HH:MM:SS
print("Current time:", today.strftime("%H:%M:%S"))