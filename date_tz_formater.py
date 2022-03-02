import datetime
from lib2to3.pytree import convert


def get_current_datetime_jst():
    return datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=6)))


def date_to_int(date)->int:
    '''
    input date object in the format of "YYYYMMDD HHMMSSffff (UTC+09:00)"
        :ex 2022-03-02 01:09:29.496387-09:00
    output int in the format of "YYYYMMDDHHMMSSffff+sign+timezone"
    '''
    # print(f"input date: {date}")
    date_with_time_zone = date.strftime("%Y%m%d%H%M%S%f%z")
    # print(date_with_time_zone)

    dates = []
    # 0 for +, 1 for - 
    sign  = 0
    if "+" in date_with_time_zone:
        dates = date_with_time_zone.split("+")
        sign = "0"
    elif "-" in date_with_time_zone:
        dates = date_with_time_zone.split("-")
        sign = "1"

    date_str = ""
    if len(dates) == 2:
        date_str = dates[0]
        time_zone = dates[1]
        date_str = date_str.replace("T", " ")
        date_str = date_str.replace("Z", "")
        date_str = date_str.replace(".", "")
        date_str = date_str.replace(" ", "")
        date_str = date_str + sign + time_zone
        # print(f"date_str: {date_str}")
    else:
        date_str = date_with_time_zone
        date_str = date_str.replace("T", " ")
        date_str = date_str.replace("Z", "")
        date_str = date_str.replace(".", "")
        date_str = date_str.replace(" ", "")
        print(f"else date_to_int: {date_str}, len: {len(date_str)}")

    return int(date_str)

#cover an int in the format of "YYYYMMDDHHMMSSffff+sign+timezone" to date object
def int_to_date(date_int):
    print(f"date_int: {date_int}")
    #2022030203030780953310900
    date_str = str(date_int)
    print(f"len(date_str): {len(date_str)}")
    if len(date_str) == 8:
        return datetime.datetime.strptime(date_str, "%Y%m%d")
    if len(date_str) == 14:
        return datetime.datetime.strptime(date_str, "%Y%m%d%H%M%S")
    elif len(date_str) == 20:
        return datetime.datetime.strptime(date_str, "%Y%m%d%H%M%S%f")
    elif len(date_str) > 18:
        year = date_str[:4]
        month = date_str[4:6]
        day = date_str[6:8]
        hour = date_str[8:10]
        minute = date_str[10:12]
        second = date_str[12:14]
        microsecond = date_str[14:20]
        time_zone = date_str[20:]
        print(f"year: {year}, month: {month}, day: {day}, hour: {hour}, minute: {minute}, second: {second}, microsecond: {microsecond}, time_zone: {time_zone}")
        if len(time_zone) == 5:
            sign = time_zone[0]
            hh = time_zone[1:3]
            mm = time_zone[3:] 
            print(f"sign: {sign}, hh: {hh}, mm: {mm}")
            if sign == "0":
                return datetime.datetime(int(year), int(month), int(day), int(hour), int(minute), int(second), int(microsecond), datetime.timezone(datetime.timedelta(hours=int(hh), minutes=int(mm))))
            elif sign == "1":
                return datetime.datetime(int(year), int(month), int(day), int(hour), int(minute), int(second), int(microsecond), datetime.timezone(datetime.timedelta(hours=-int(hh), minutes=-int(mm))))
        else:
            return datetime.datetime(int(year), int(month), int(day), int(hour), int(minute), int(second), int(microsecond))
    else:
        return datetime.datetime.strptime(date_str, "%Y%m%d%H%M%S%f")

#date to timestamp
def date_to_timestamp(date):
    return date.timestamp()

#timestamp to date
def timestamp_to_date(timestamp):
    return datetime.datetime.fromtimestamp(timestamp)

if __name__ == "__main__":
    date_obj = get_current_datetime_jst()
    print(f"date_to_timestamp: {date_to_timestamp(date_obj)}")
    # date_s = "2022-03-02"
    # get date object from date_s in the format of "YYYY-MM-DD"
    # date_obj = datetime.datetime.strptime(date_s, "%Y-%m-%d")
    print(f"date_obj: {date_obj}")
    # print(f"int to date: {int_to_date(date_to_int(date_obj))}")
    date_convert = int_to_date(date_to_int(date_obj))
    print(f"date_convert: {date_convert}")
    assert date_obj == date_convert
