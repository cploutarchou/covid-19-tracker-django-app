import datetime

today = datetime.datetime.now()
given_date = today.date()


class CurrentMonth:
    def __init__(self):
        self.current_month = today.strftime("%B")
        self.current_month_first_date = given_date.replace(day=1).strftime("01-%m-%Y")
        self.today_date_str = today.strftime('%d-%m-%Y')

    def get_current_month(self):
        return self.current_month

    def get_today_date(self):
        return self.today_date_str

    def get_current_month_first_date(self):
        return self.current_month_first_date
