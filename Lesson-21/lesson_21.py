from classes import statistics, PersonAccount as PA

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24,
        32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

data = statistics(ages)
print("\n--- Describe Method Output ---")
print(data.describe())

p = PA("Muhammad", "Umais", {"1": 1000, "2": 1500, "3": 700},
       {"Rent": 1200, "Fee": 600, "Utility": 1300})

print(p.account_info())
print(p.total_income())
print(p.total_expense())
print(p.account_balance())
p.add_income("4", 2000)
p.add_expense("living", 1700)
print(p.total_income())
print(p.total_expense())
print(p.account_balance())
print(p.account_info())
