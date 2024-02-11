#10. Write a Python program to calculate the number of days between two dates.

from datetime import date
firstdate = date(2020, 6, 10)
lastdate = date(2020, 12, 12)

betweendates = lastdate-firstdate

print(betweendates.days)
