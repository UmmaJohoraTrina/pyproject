import calendar

print(calendar.weekheader(3))
print()

print(calendar.firstweekday())
print()

print(calendar.month(2020, 10))

print(calendar.calendar(2020))

is_leap = calendar.isleap(2020)
print(is_leap)

how_many_leap_days=calendar.leapdays(2000,2021)
print(how_many_leap_days)
