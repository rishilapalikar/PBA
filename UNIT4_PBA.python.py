import pandas as pd
import matplotlib.pyplot as plt

# Read employee details from CSV file
df = pd.read_csv("employee.csv")

# Display employee names, departments and salaries
print("Employee Details:")
print(df[['Name', 'Department', 'Salary']])

# Calculate average salary for each department
avg_salary = df.groupby('Department')['Salary'].mean()

print("\nAverage Salary of Each Department:")
print(avg_salary)

# Plot average salary of each department
avg_salary.plot(kind='bar', color='skyblue')
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.tight_layout()
plt.show()