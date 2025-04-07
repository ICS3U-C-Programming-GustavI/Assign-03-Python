#!/usr/bin/env python3
# Created by: Gustav I
# Created on: April 7, 2025
# This program asks the user to enter a month and a year,
# then tells them how many days are in that month.
# If the month is February, it checks for a leap year and adjusts the days.

from month_days import ( # Import month info from external file
    month_days, 
    valid_months,
  )  


def main():
    print("This program tells you how many days are in a month and checks the year.")
    print(
        "Note: Please enter the month with the first letter capitalized and do not add a space after your month (e.g., February).\n"
    )

    # Ask the user for the month
    user_month = input("Enter the name of a month: ")

    # Check if the entered month is valid
    if user_month not in valid_months:
        print("Invalid month! Please restart and enter a valid month name.")
        return  # Exit early if the month isn't in our list

    # Ask the user for the year
    user_year_input = input("Enter a year (e.g., 2024): ")

    try:
        user_year = int(user_year_input)  # Try converting year to integer
    except ValueError:
        print("Invalid year! Please restart and enter a number.")
        return

    # Check for February and leap year logic
    if user_month == "February":
        # Nested if with Boolean operators for leap year
        if (user_year % 4 == 0 and user_year % 100 != 0) or (user_year % 400 == 0):
            print(f"There are 29 days in {user_month} of {user_year} (leap year).")
        else:
            print(
                f"There are 28 days in {user_month} of {user_year} (not a leap year)."
            )
    else:
        # For all other months, use the dictionary value directly
        print(
            f"There are {month_days[user_month]} days in {user_month} of {user_year}."
        )


# Only run if this file is executed directly
if __name__ == "__main__":
    main()
