import pandas as pd
import matplotlib.pyplot as plt

plt.switch_backend('Agg')

data = pd.read_csv (r'C:\Users\Ilyapro163\Desktop\Student Exam Scores.csv')


data[['FirstName', 'LastName']] = data['Name'].str.split(" ", expand=True)

data['ExamDate'] = pd.to_datetime(data['ExamDate']).dt.strftime('%Y-%m-%d')

data['TotalScore'] = data['MathScore'] + data['ReadingScore'] + data['WritingScore']

filtred_data = data[(data['IsFirstChild'] == 'Yes') & (data['NrSiblings'] > 2)]

sorted_data = filtred_data.sort_values(by='ExamDate', ascending=False)

highlighted_data = sorted_data[sorted_data['WklyStudyHours'] > 10]

highlighted_data['Color'] = highlighted_data['TotalScore'].apply(lambda x: 'red' if x < 60 else 'green' if x > 90 else 'yellow' )

average_scares = data.groupby('Gender')['TotalScore'].mean()
average_scares.plot(kind='bar', color=['blue', 'pink'])

plt.title('Средний суммарный балл по полу')
plt.xlabel('Пол')
plt.ylabel('Средний балл')

plt.savefig('average_scores_by_gender.png')
