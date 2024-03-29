basic_salary = float(input("Enter your basic salary: "))
gross_salary = (basic_salary + basic_salary * 0.1 + basic_salary * 0.9) if basic_salary < 1500 else (
            basic_salary + basic_salary * 0.98 + 500)
print(f"Your salary is: {gross_salary} Rs.")
