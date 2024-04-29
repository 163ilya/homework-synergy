import pandas as pd

file_path = 'C:/Users/ilyapro163/Desktop/Продажи.csv'
data = pd.read_csv(file_path)

print('Исходные данные:')
print(data.head())

data['Дата'] = pd.to_datetime(data['Дата'], format='%m/%d/%Y')

data['Номер недели'] = data['Дата'].dt.isocalendar().week

print('\nДанные после добавления номера недели:')
print(data[['Дата', 'Номер недели']].head())

output_file_path = 'C:/Users/ilyapro163/Desktop/Продажи.csv'
data.to_csv(output_file_path, index=False)
print(f"\nОбработанные данные сохранены в файл: {output_file_path}")
