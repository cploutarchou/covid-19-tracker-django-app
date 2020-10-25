import datetime
import time


class GeneralFunctions(object):
    @staticmethod
    def percentage_difference_calculator(old_value, new_value):
        val1 = float(old_value)
        val2 = float(new_value)
        rate = (((val1 - val2) / ((val1 + val2) / 2)) * 100)
        if rate is not None:
            return format(--rate, ".2f")
        else:
            return False


class Dates:

    @staticmethod
    def query_date(days_difference: int = None) -> datetime:
        return datetime.date.today() - datetime.timedelta(days=days_difference)

    @staticmethod
    def get_current_datetime(date_string, str_format="%Y-%m-%d") -> datetime:
        # Expects "YYYY-MM-DD" string
        # returns a datetime object
        e_seconds = time.mktime(time.strptime(date_string, str_format))
        return datetime.datetime.fromtimestamp(e_seconds)

    @staticmethod
    def format_date(input_datetime, str_format="%Y-%m-%d") -> time.strftime:
        # format a datetime object as YYYY-MM-DD string and return
        return input_datetime.strftime(str_format)

    @staticmethod
    def get_current_month_first_day(input_datetime):
        # what is the first day of the current month
        days = int(input_datetime.strftime("%d")) - 1  # days to subtract to get to the 1st
        delta = datetime.timedelta(days=days)  # create a delta datetime object
        return input_datetime - delta  # Subtract delta and return

    @staticmethod
    def get_current_month_first_day_2(input_datetime):
        return Dates.get_current_datetime(Dates.format_date(input_datetime, "%Y-%m-01"))

    @staticmethod
    def get_current_month_last_day(input_datetime) -> datetime:
        year = input_datetime.strftime("%Y")  # get the year
        month = str(int(input_datetime.strftime("%m")) % 12 + 1)
        date = "1"  # first day of next month
        next_month = Dates.get_current_datetime(
            "%s-%s-%s" % (year, month, date))  # make a datetime obj for 1st of next month
        delta = datetime.timedelta(seconds=1)  # create a delta of 1 second
        return next_month - delta  # subtract from next_month and return

    @staticmethod
    def get_yesterday_date() -> time.strftime:
        yesterday = Dates.query_date(3)
        yesterday = yesterday.strftime('%Y-%m-%d')
        return yesterday

    @staticmethod
    def get_two_dates_before() -> time.strftime:
        res = Dates.query_date(4)
        res = res.strftime('%Y-%m-%d')
        return res
