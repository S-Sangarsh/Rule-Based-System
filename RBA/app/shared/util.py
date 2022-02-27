from datetime import datetime
import pytz



class DateTimeUtil:
    @staticmethod
    def current_date_time():
        tz = pytz.timezone("Asia/Kolkata")
        return datetime.now(tz)

