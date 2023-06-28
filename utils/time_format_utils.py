import re


# 1.匹配时间2019-11-20T10:06:09+08:00
def verify_datetime(datetime_):
    pattern = r'((?!0000)[0-9]{4}-((0[1-9]|1[0-2])-(0[1-9]|1[0-9]|2[0-8])|(0[13-9]|1[0-2])-(29|30)|(0[13578]|1[02])-31)|([0-9]{2}(0[48]|[2468][048]|[13579][26])|(0[48]|[2468][048]|[13579][26])00)-02-29) (20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d$'
    if re.match(pattern, datetime_):
        return True


# 2.处理匹配到的时间
def format_date_tz(raw_date):
    date = raw_date.replace('T', ' ').replace('Z', '').split('+')[0].split('.')[0]
    if not verify_datetime(date):
        raise ValueError(raw_date, date)
    return date
