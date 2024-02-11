#1. A company decides to give a bonus of 5% to its employees if their years of service are more than 5. write a program to input their salaries and years of service and display the bonus or eligibility.

salary = float(input('Enter the salary: '))
yos = int(input('Enter the years of service: ')) #years of service

nsalary = salary*0.05 #new salary

if yos>=5:
    print(f'Your eligible for get the bonus, your bonus is: ',nsalary)
else:
    print(f'Your not eligible for get the bonus ')
    

