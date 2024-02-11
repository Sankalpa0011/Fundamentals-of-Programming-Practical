#8. Accepts six numbers as input and sorts them in descending order.
      
num1 =float(input('Enter the number1: '))
num2 =float(input('Enter the number2: '))
num3 =float(input('Enter the number3: '))
num4 =float(input('Enter the number4: '))
num5 =float(input('Enter the number5: '))
num6 =float(input('Enter the number6: '))

numbers = [num1,num2,num3,num4,num5,num6]
numbers.sort(reverse=True)
print('The numbers in descending order are: ')

for number in numbers:
            print(number)
            
