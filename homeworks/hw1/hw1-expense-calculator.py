#Calculate monthly budget and saving
income = float(input("User's monthly income in THB: "))
rent = float(input("Monthly rent/housing cost: "))
food = float(input("Monthly food budget in THB: "))
transportation = float(input("Monthly transportation expenses: "))
entertainment = float(input("Monthly entertainment budget: "))
emergency_percent = float(input("Percentage to save for emergency: "))
investment_percent = float(input("Percent to invest: "))

total_fixed = rent + transportation
total_variable = food + entertainment 
total_expenses = total_fixed + total_variable
remaining_income = income - total_expenses
emergencyfund = income * (emergency_percent/100)
investment = income * (investment_percent/100)
available_saving = remaining_income - emergencyfund - investment
expense_ratio = (total_expenses/income)*100

print(f"=== MONTHLY BUDGET REPOST ===")
print(f"Income: {income:.2f} THB")
print(f"Fixed Expenses: {total_fixed:.2f} THB")
print(f"Variable Expenses : {total_variable:.2f} THB")
print(f"Total Expenses: {total_expenses:.2f} THB")
print(f"Remaining: {remaining_income:.2f} YHB")
print()
print("=== SAVINGS BREAKDOWN ===")
print(f"Emergency Fund ({emergency_percent}) : {emergencyfund:.2f} THB")
print(f"Investment ({investment_percent}) : {investment:.2f} THB")
print(f"(Available for Savings : {available_saving:.2f} THB")
print()
print("=== ANALYSIS ===")
print(f"Expense Ratio : {expense_ratio:.2f}%")