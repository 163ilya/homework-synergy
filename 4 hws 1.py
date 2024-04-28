import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv(r'C:\Users\Ilyapro163\Desktop\supermarket_sales.csv', delimiter=';', encoding='latin-1')

data['Date'] = pd.to_datetime(data['Date'], errors='coerce', format='%m/%d/%Y')
data['Date'] = pd.to_datetime(data['Date'], errors='coerce', format='%d.%m.%y')

if data['Date'].isnull().any():
    print("Some dates could not be parsed.")
  
print(data.info())

data['Total'] = data['Total'].str.replace(r'[^\d.]', '', regex=True).astype(float)
data['cogs'] = data['cogs'].str.replace(r'[^\d.]', '', regex=True).astype(float)

print(data.columns)
print(data.dtypes)

data['Date'] = pd.to_datetime(data['Date'], format='%d.%m.%y')

data['Day'] = data['Date'].dt.day
data['Month'] = data['Date'].dt.month
data['Year'] = data['Date'].dt.year

sales_by_day = data.groupby('Day')['Total'].sum()
sales_by_month = data.groupby('Month')['Total'].sum()
sales_by_year = data.groupby('Year')['Total'].sum()

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
sales_by_day.plot(kind='bar', color='skyblue')
plt.title('Total Sales by Day')
plt.xlabel('Day')
plt.ylabel('Total Sales')

plt.subplot(1, 3, 2)
sales_by_month.plot(kind='bar', color='lightgreen')
plt.title('Total Sales by Month')
plt.xlabel('Month')
plt.ylabel('Total Sales')

plt.subplot(1, 3, 3)
sales_by_year.plot(kind='bar', color='salmon')
plt.title('Total Sales by Year')
plt.xlabel('Year')
plt.ylabel('Total Sales')

plt.tight_layout()
plt.show()
