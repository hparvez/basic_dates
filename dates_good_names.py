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

    def __init__(self, date):
        self.date: str = date
        self.day: str = date.split("/")[0]
        self.month: str = date.split("/")[1]
        self.month_name: str = MONTH_TO_YEAR[self.month]
        self.year: str = date.split("/")[2]

    def __str__(self) -> str:
        return f"{self.day} of {self.month_name}, {self.year}"

    def is_leap_year(self) -> bool:
        return int(self.year) % 4 == 0

    def get_day_adjustment(self) -> int:
        year = int(self.year)
        if 2000 <= year <= 2099:
            return -1
        else:
            return 0

    def get_day_of_week(self) -> int:
        year_digits = int(self.year[2:])
        month_key_number = MONTH_KEY[self.month_name]

        if self.is_leap_year():
            if self.month_name == "January" or self.month_name == "February":
                month_key_number -= 1

        day_adjustment = self.get_day_adjustment()

        return (year_digits + int(year_digits / 4) + month_key_number +
                int(self.day) + day_adjustment) % 7

    def get_day_name(self) -> str:
        return DAY_NUMBER_TO_NAME[self.get_day_of_week()]

    def is_weekend(self) -> bool:
        day_name = self.get_day_name()
        if day_name == "Saturday" or day_name == "Sunday":
            return True
        else:
            return False
