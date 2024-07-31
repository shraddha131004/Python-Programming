import calendar
year = int(input('Enter the year:'))
mon = int(input('Enter the month:'))

my_cal = calendar.month(year,mon)
print(my_cal)