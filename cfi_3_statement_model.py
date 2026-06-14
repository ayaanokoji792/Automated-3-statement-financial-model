import pandas as pd
import matplotlib.pyplot as plt

years = ['2023', '2024', '2025E', '2026E', '2027E']
assumptions = {
    'Revenue_Growth': [0, 0.15, 0.12, 0.10, 0.08], # here, E stand for estimated
    'COGS_Margin': [0.40, 0.38, 0.38, 0.37, 0.36]
}

df = pd.DataFrame(assumptions, index=years)
df['Revenue'] = [1000, 1150, 0, 0, 0] 

for i in range(2, 5): 

    df.loc[years[i], 'Revenue'] = df.loc[years[i-1], 'Revenue'] * (1 + df.loc[years[i], 'Revenue_Growth'])

df['COGS'] = df['Revenue'] * df['COGS_Margin']
df['Gross_Profit'] = df['Revenue'] - df['COGS']
df['Gross_Margin'] = df['Gross_Profit'] / df['Revenue']

df = df.round(2)
print(df[['Revenue', 'COGS', 'Gross_Profit', 'Gross_Margin']])



fig, ax1 = plt.subplots(figsize=(10, 5))

ax1.bar(df.index, df['Revenue'], color='lightsteelblue', label='Revenue')
ax1.set_ylabel('Revenue ($)', color='black')

ax2 = ax1.twinx()
ax2.plot(df.index, df['Gross_Margin'], color='midnightblue', marker='o', linewidth=2, label='Gross Margin')
ax2.set_ylabel('Gross Margin (%)', color='midnightblue')

plt.title('5-Year Revenue & Gross Margin Forecast')
plt.savefig('chart.png') 
print("saved")