# month_days.py
# This module holds the number of days in each month (excluding leap year adjustment for February)

month_days = {
    "January": 31,
    "February": 28,  # February's days are updated in main.py if it's a leap year
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31,
}

# List of valid months (used for checking valid input)
valid_months = list(month_days.keys())
