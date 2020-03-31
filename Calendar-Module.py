# Python Calendar Module HackerRank solution

import calendar

day,month,year=map(int,input().split())
print(calendar.day_name[calendar.weekday(year,day,month)].upper())