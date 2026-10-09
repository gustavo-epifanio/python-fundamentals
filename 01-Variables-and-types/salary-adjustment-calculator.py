#Program that adjust your salary
salary = float(input('Enter your salary: '))
salary_increase = float(input('Enter the percentage of increase on your salary (Numbers only): '))
new_salary = salary + (salary * salary_increase/100)
print('Your new salary is: ${}'.format(new_salary))