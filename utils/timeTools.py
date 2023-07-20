import math
from datetime import timezone, datetime


class TimeTools:
    @staticmethod
    def formatTimestamp(timestamp, fmt="%Y-%m-%d %H:%M:%S", tz=None):
        """将时间戳转换为 UTC 时间"""
        digits = int(math.log10(timestamp)) + 1
        if digits == 13:
            timestamp = timestamp / 1000
        return datetime.fromtimestamp(timestamp, tz).strftime(fmt)

    @staticmethod
    def timeStamp(dateString, tz=None):
        num = dateString.count(":")
        fmt = "%Y-%m-%d %H:%M:%S"
        if num == 0:
            fmt = "%Y-%m-%d"
        elif num == 1:
            fmt = "%Y-%m-%d %H:%M"
        elif num == 2:
            fmt = "%Y-%m-%d %H:%M:%S"
        utc_dt = datetime.strptime(dateString, fmt).replace(tzinfo=tz)
        return int(utc_dt.timestamp())
