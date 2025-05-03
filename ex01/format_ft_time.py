import datetime

begin_t = datetime.datetime(1970, 1, 1)
now_t = datetime.datetime.now()

# convert to seconds
year_sec = ((now_t.year - begin_t.year) * 31536000)
month_sec = ((now_t.month - begin_t.month) * 2629800)
day_sec = ((now_t.day - begin_t.day) * 86400)
hour_sec = ((now_t.hour - begin_t.hour) * 3600)
minute_sec = ((now_t.minute - begin_t.minute) * 60)
sec = (now_t.second - begin_t.second)
# micro to seconds
mill_sec = ((now_t.microsecond - begin_t.microsecond) * 0.000001)

rslt_sec = year_sec + month_sec + day_sec + hour_sec + minute_sec + sec + mill_sec

print("Seconds since", begin_t.strftime("%B"), begin_t.day, ",", begin_t.year, ":", rslt_sec,"or", f"{rslt_sec:.2e}", "in scientific notation")

print(now_t.strftime("%b"),now_t.strftime("%d"), now_t.year)