from datetime import datetime

class Session:

    def __init__(self, session_id: int, customer_id: int, expire_date_time: str):
        self.session_id = session_id
        self.customer_id = customer_id
        self.expire_date_time = expire_date_time

    @staticmethod
    def convert_expire_date_time(self) -> datetime:
        date_and_time_separated = self.expire_date_time.split(" ")
        date = date_and_time_separated[0]
        date_separated = date.split("-")
        year = int(date_separated[0])
        month = int(date_separated[1])
        day = int(date_separated[2])
        time = date_and_time_separated[1]
        time_separated = time.split(":")
        hour = int(time_separated[0])
        minute = int(time_separated[1])
        seconds_and_microseconds = time_separated[2].split(".")
        seconds = int(seconds_and_microseconds[0])
        microseconds = int(seconds_and_microseconds[1])
        return datetime(year, month, day, hour, minute, seconds, microseconds)
