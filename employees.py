import pandas as pd
import datetime

employees = pd.read_csv('employees.csv')

engineering = employees[(employees['Department'] == 'Engineering') & 
                        (employees['PerformanceScore'] >= 7)
                        ]

engineering.to_csv('top_engineers.csv')

avg_employees = employees.groupby('Department')['Salary'].mean()

employees['JoiningDate'] = pd.to_datetime(employees['JoiningDate'])

old_employees = employees[(employees['JoiningDate'] < '2018-01-01') & 
                          (employees['Age'] > 30)]

today = pd.to_datetime('today')

employees['YearsAtCompany'] = (today - employees['JoiningDate']).dt.days // 365

sorted_employees = employees.sort_values(
  by=['PerformanceScore', 'Salary'],
  ascending=[False, True]
)

avg_performance = employees.groupby('Department')['PerformanceScore'].mean()
print(avg_performance)

top_dept = avg_performance.idxmax()
print(f"the dept. the highest average performance score is: {top_dept} ")