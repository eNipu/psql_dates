
import datetime
from lib2to3.pytree import convert

#covert a date to a string in the format of "YYYY-MM-DD"
def date_formater(date):
    return date.strftime("%Y-%m-%d")

#covert a string in the format of "YYYY-MM-DD" to a date
def date_parser(date_str):
    return datetime.datetime.strptime(date_str, "%Y-%m-%d")


#covert a date to a string in the format of "YYYY-MM-DD HH:MM:SS"
def datetime_formater(date):
    return date.strftime("%Y-%m-%d %H:%M:%S")

#covert a string in the format of "YYYY-MM-DD HH:MM:SS" to a date
def datetime_parser(date_str):
    return datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")


#covert a date to a string in the format of "YYYY-MM-DD HH:MM:SS.SSS"
def datetime_ms_formater(date):
    return date.strftime("%Y-%m-%d %H:%M:%S.%f")

#covert a string in the format of "YYYY-MM-DD HH:MM:SS.SSS" to a date
def datetime_ms_parser(date_str):
    return datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")

#covert a date to a string in the format of "YYYY-MM-DD HH:MM:SS.SSS Z"
def datetime_ms_tz_formater(date):
    return date.strftime("%Y-%m-%d %H:%M:%S.%f %Z")


#pass a date and time string in the format of "YYYY-MM-DD HH:MM:SS.SSS Z" and return a datetime object with japanese timezone
def datetime_ms_tz_parser(date_str):
    print(date_str)
    #split the date_str for getting the timezone
    date_str_list = date_str.split(" ")
    #get the timezone
    timezone = date_str_list[-1]
    print(f"timezone: {timezone}")
    #get the date
    date_str = " ".join(date_str_list[:-1])
    #convert the date to datetime object
    date = datetime_ms_parser(date_str)
    #convert the timezone to datetime object
    timezone = datetime.datetime.strptime(timezone, "%z")
    #convert the datetime object to japanese timezone
    return date.astimezone(timezone)


#parse UTC+09:00 to datetime object
def parse_utc_jst(date_str):
    return datetime.datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f%z")

# parse 2022-03-02 17:43:20.953364 UTC+09:00 to datetime object
def parse_utc_jst_ms(date_str):
    return datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f%z")

#get the current date and time with japanese timezone
def get_current_datetime_jst():
    return datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))

#convert date object to int in the format of "YYYYMMDD HHMMSS (UTC+09:00)"
def date_to_int(date):
    return int(date.strftime("%Y%m%d%H%M%S%f"))

#cover a date of 2022-03-02 17:58:41.783591+09:00 to int in the format of "YYYYMMDD HHMMSS (UTC+09:00)"
def date_to_int_ms(date):
    date_with_time_zone = date.strftime("%Y%m%d%H%M%S%f%z")
    print(date_with_time_zone)
    dates = []
    if "+" in date_with_time_zone:
        dates = date_with_time_zone.split("+")
    if "-" in date_with_time_zone:
        dates = date_with_time_zone.split("-")
    if len(dates) == 2:
        date_str = dates[0]
        time_zone = dates[1]
        date_str = date_str.replace("T", " ")
        date_str = date_str.replace("Z", "")
        date_str = date_str.replace(".", "")
        date_str = date_str.replace(" ", "")
        date_str = date_str[:14]
        date_str = date_str + time_zone
        date = datetime_ms_tz_parser(date_str)
        return date_to_int_ms(date)
    
    # date_without_time_zone = dates[0]
    # time_zone = dates[1]
    # time_zone_hour = time_zone[0:2]
    # time_zone_minute = time_zone[2:4]
    # #convert the date to int
    # date_int = int(date_without_time_zone)
    # #convert the time zone to int
    # time_zone_int = int(time_zone)
    # print(f"time_zone_int: {time_zone_int}")
    # return date_int + time_zone_int

#convert integet in the format of "YYYYMMDD HHMMSS (UTC+09:00)" to date object
def int_to_date(date_int):
    print(f"date_int: {date_int}")
    date_str = str(date_int)
    print(f"len(date_str): {len(date_str)}")
    if len(date_str) == 14:
        return datetime.datetime.strptime(date_str, "%Y%m%d%H%M%S")
    elif len(date_str) == 15:
        return datetime.datetime.strptime(date_str, "%Y%m%d%H%M%S%f")
    elif len(date_str) == 16:
        return datetime.datetime.strptime(date_str, "%Y%m%d%H%M%S%f%z")
    elif len(date_str) == 17:
        return datetime.datetime.strptime(date_str, "%Y%m%d%H%M%S%f%z")
    else:
        return None
    # year = date_str[:4]
    # month = date_str[4:6]
    # day = date_str[6:8]
    # hour = date_str[8:10]
    # minute = date_str[10:12]
    # second = date_str[12:14]
    # microsecond = date_str[14:18]
    # time_zone = date_str[18:]
    # print(f"time_zone: {time_zone}")
    # return datetime.datetime(int(year), int(month), int(day), int(hour), int(minute), int(second), int(microsecond), datetime.timezone(datetime.timedelta(hours=9)))
#test all the functions
if __name__ == "__main__":
    date = get_current_datetime_jst()
    print(f"date: {date}")
    print(f"int: {date_to_int_ms(date)}")
    # print(f"int: {date_to_int_ms(date)}")
    # print(f"date: {int_to_date(date_to_int(date))}")
    # print(date_to_int(date))
    # date_str = datetime_ms_tz_formater(date)
    # print(str(date))
    # print(parse_utc_jst_ms(date_str))
