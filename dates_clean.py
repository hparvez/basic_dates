MONTH_TO_YEAR = {
    "01": "January", "02": "February", "03": "March",
    "04": "April", "05": "May", "06": "June", "07": "July",
    "08": "August", "09": "September", "10": "October",
    "11": "November", "12": "December"
    }

MONTH_KEY = {
    "January": 1, "February": 4, "March": 4, "April": 0,
    "May": 2, "June": 5, "July": 0, "August": 3, "September": 6,
    "October": 1, "November": 4, "December": 6
}

DAY_NUMBER_TO_NAME = {
    1: "Sunday", 2: "Monday", 3: "Tuesday", 4: "Wednesday",
    5: "Thursday", 6: "Friday", 0: "Saturday"
}


class Date(object):
    """
    Class to work with dates. Input date must be of
    the form dd/mm/yyyy, and must be between 01/01/1900
    and 31/12/2099
    """
    def __init__(self, date):
        self.date: str = date
        self.day: str = date.split("/")[0]
        self.month: str = date.split("/")[1]
        self.month_name: str = MONTH_TO_YEAR[self.month]
        self.year: str = date.split("/")[2]

    def __str__(self) -> str:
        return f"{self.day} of {self.month_name}, {self.year}"

    def is_leap_year(self) -> bool:
        """
        Function to check if the date falls within a leap year
        Note: it is assumed that a leap year occurs whenever our year
        is divisible by four with no remainder

        Returns:
            bool: returns True if this is a leap year, False otherwise
        """
        return int(self.year) % 4 == 0

    def get_day_adjustment(self) -> int:
        """
        Fnuction that determines the "day" adjustment within the
        day-of-the-week calculation

        Returns:
            int: -1 if year is between 2000 and 2099, 0 otherwise
        """
        year = int(self.year)
        if 2000 <= year <= 2099:
            return -1
        else:
            return 0

    def get_day_of_week(self) -> int:
        """
        Function to return the day of the week as an integer. Uses the
        following components:
        'year_digits': last 2 digits of the year, e.g. 2022 would be 22
        'int(year_digts / 4)': the integer part of the above divided by 4, e.g.
        2022 would become (2022 / 4) = 505.5 -> 505
        'month_key_number': a weighting key applied to each month
        'day': day of current month
        'day_adjustment': deducting 1 if the year is between 2000 and 2099

        Formula is as follows:
        (last 2 digits of year) +
        (integer part of (last 2 digits of year / 4)) +
        (month key number) +
        (day of month) +
        (day adjustment) % 7

        Returns:
            int: integer representing day of the week. Possible answers are:
            0 - Saturday
            1 - Sunday
            2 - Monday
            3 - Tuesday
            4 - Wednesday
            5 - Thursday
            6 - Friday
        """
        # Final 2 digits of the year, e.g. 2022 -> 22
        year_digits = int(self.year[2:])
        month_key_number = MONTH_KEY[self.month_name]

        # Adjust for leap years
        if self.is_leap_year():
            if self.month_name == "January" or self.month_name == "February":
                month_key_number -= 1

        day_adjustment = self.get_day_adjustment()

        return (year_digits + int(year_digits / 4) + month_key_number +
                int(self.day) + day_adjustment) % 7

    def get_day_name(self) -> str:
        """
        Function that converts an integer representation of a day to its string

        Returns:
            str: name of the weekday representing by the integer
        """
        return DAY_NUMBER_TO_NAME[self.get_day_of_week()]

    def is_weekend(self) -> bool:
        """
        Function to check if the date falls on a weekday or a weekend

        Returns:
            bool: True if its a weekend, False otherwise
        """
        day_name = self.get_day_name()
        if day_name == "Saturday" or day_name == "Sunday":
            return True
        else:
            return False
