#9. Print the calendar of a given month and year.(used user input for getting year and month)

import calendar

year = int(input('Enter the year: '))
month = int(input('Enter the month: '))

print(calendar.month(year,month))
