import calendar


year = 2021
month = 6

print(calendar.month(year, month))

cal = calendar.HTMLCalendar(firstweekday=0)

file = cal.formatmonth(2020, 9, withyear=True)
with open("index.html", "w") as f:
    f.write(file)

print("Сколько високосных годов в интервале: ",  alendar.leapdays(2020, 2021))
print("Високосный год ?",  calendar.isleap(2020))


