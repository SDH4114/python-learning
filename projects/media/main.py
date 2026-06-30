import pandas as po  # импортируем библиотеку pandas и даем ей короткое имя po

def check(data):
    print(data)
    print("")

# Читаем CSV-файл data.csv и превращаем его в DataFrame
data = po.read_csv('data.csv')
check(data)

# В колонке Views заменяем пустые значения NaN на среднее значение этой колонки
data["Views"] = data['Views'].fillna(data['Views'].mean())

# В колонке Revenue заменяем пустые значения NaN на 0
data["Revenue"] = data['Revenue'].fillna(0)
check(data)

# Удаляем полностью одинаковые строки, если такие есть
# inplace=True значит: изменить эту же таблицу, а не создавать новую
data.drop_duplicates(inplace=True)
check(data)

# Меняем тип данных в колонке Views на int, то есть на целые числа
data['Views'] = data['Views'].astype(int)

# Превращаем колонку Date из обычного текста в настоящий тип даты datetime
data["Date"] = po.to_datetime(data['Date'])
check(data)

# Показываем статистику по числовым колонкам: count, mean, min, max и т.д.
check(data.describe())

filtred = data[data['Platform'] == "YouTube"]
check(filtred)

grouped = filtred.groupby('Date').agg({'Views': 'sum', 'Revenue':'sum'}).reset_index()

check(grouped)


mean_views = grouped['Views'].mean()
mean_revenue = grouped['Revenue'].mean()

print(f"Mean views - {mean_views}, mean revenue - {mean_revenue}")


data.to_csv('main_data.csv', index = False)
grouped.to_csv('yt.csv', index = False)
