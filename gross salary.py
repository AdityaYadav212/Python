basic_salary = int(input("Enter your basic salary: "))

if basic_salary > 20000:

   hra = .30 * basic_salary

   da = .95 * basic_salary

elif basic_salary <= 20000:

   hra = .25 * basic_salary

   da = .90 * basic_salary

else:

   hra = .20 * basic_salary

   da = .80 * basic_salary

gross_salary = basic_salary + hra + da

print(f"The gross salary is {gross_salary}.")