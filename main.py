from datetime import datetime, timedelta

def handle_date_format(time):
    date = time    
    date = date.replace('T', ' ')
    date = date.replace('Z', '')
    date = date[0:18]
    date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    
    return date

def utc_to_cst(time):
    utc_date_and_time = time
    hours = -5
    hours_added = timedelta(hours = hours)
    cst_date_and_time = utc_date_and_time + hours_added

    return cst_date_and_time

date = '2021-08-11T20:10:09.040336401Z'

print(utc_to_cst(datetime.utcnow()).strftime("%Y-%m-%d %H:%M:%S CST"))
date = handle_date_format(date)
print(utc_to_cst(date))
date = datetime.strftime(utc_to_cst(date), "%Y-%m-%dT%H:%M:%S")
print(date)