import math
from datetime import timezone, datetime

class TimeTools:
    @staticmethod
    def formatTimestamp(timestamp,fmt="%Y-%m-%d",tz=None):
        """将时间戳转换为 UTC 时间"""
        digits = int(math.log10(timestamp)) + 1
        if digits == 13:
            timestamp = timestamp / 1000
        return datetime.fromtimestamp(timestamp,tz).strftime(fmt)

    @staticmethod
    def timeStamp(dateString, tz=None, fmt="%Y-%m-%d"):
        utc_dt = datetime.strptime(dateString, fmt).replace(tzinfo=tz)
        return int(utc_dt.timestamp())