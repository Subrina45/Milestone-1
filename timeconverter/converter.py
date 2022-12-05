from datetime import datetime
from time import mktime


class TimeConverter():

    def format_unixtimestamp(self, time, time_type):
        dt = datetime.strptime(time + ' ' + time_type, "%I:%M %p")
        dt = dt.replace(1970, 1, 1)
        return int(mktime(dt.timetuple()))

    def format_humanreadable(self, timestamp, include_type = True):
        return datetime.fromtimestamp(int(timestamp)).strftime("%I:%M %p" if include_type else "%I:%M")

    def date_to_unixtimestamp(self, date):
        """Transform a date represented as mm/dd/yyyy to unixtimestamp
        """
        formated_date = datetime.strptime(date, "%m/%d/%Y")
        return int(mktime(formated_date.timetuple()))

    def unixtimestamp_to_date(self, timestamp):
        """format a unix timestamp to a day written as mm/dd/yyyy 
        """
        return datetime.fromtimestamp(int(timestamp)).strftime("%m/%d/%Y")
