import pandas as pd

data = pd.read_csv(r'C:\Users\Ilyapro163\Desktop\Yacht.csv')


data[['Currency', 'PriceValue']] = data['Price'].str.extract(r'([A-Za-z]+)\s([\d.,]+)')

data['PriceValue'] = data['PriceValue'].str.replace(".", "").str.replace(",", "").astype(float)

print("Price and Currency extraction:")
print(data[['PriceValue', 'Currency']].head())

currency_rates = {'EUR': 85.0, 'CHF': 78.0}
data['PriceInRubles'] = data.apply(lambda row: row['PriceValue'] * currency_rates.get(row['Currency'], 1), axis=1)

print("Price conversion to Rubles:")
print(data[['PriceInRubles']].head())

data['PublishDay'] = pd.to_datetime(data['Advertisement Date'], dayfirst=True).dt.dayofweek

filtred_data = data[(data['Condition'].isin(['is new', 'very good'])) & (data['PublishDay'] < 5)]

print("Filtred data:")
print(filtred_data[['Condition', 'PublishDay', 'PriceInRubles']].head())

average_price = filtred_data['PriceInRubles'].mean()
print('Средняя стоимость:', average_price)
