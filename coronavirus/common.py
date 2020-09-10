import datetime

now = datetime.datetime.now()
given_date = now.date()


class CurrentMonth:
    def __init__(self):
        self.current_month = now.strftime("%B")
        self.current_month_int = now.strftime("%m")
        self.current_month_first_date = given_date.replace(day=1).strftime("01-%m-%Y")
        self.today_date_str = now.strftime('%d-%m-%Y')

    def get_current_month(self):
        return self.current_month

    def get_today_date(self):
        return self.today_date_str

    def get_current_month_first_date(self):
        return self.current_month_first_date

    def get_current_month_int(self):
        return int(self.current_month_int)
