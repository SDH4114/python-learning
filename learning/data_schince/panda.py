import pandas as pnd

data = {
    'name':["Rent", "Raya", "Haos", "Zero", "Senky", "Tester"],
    'age':[20, 19, 19, 60, 28, 20],
    'city':["Shiner", "Poema", "Poema", "Swamp", "Tokio", "Testoland"]
}

df = pnd.DataFrame(data)
dd = pnd.Series(data) # бесполезно как будто
print(df)
#      name  age       city
# 0    Rent   20     Shiner
# 1    Raya   19      Poema
# 2    Haos   19      Poema
# 3    Zero   60      Swamp
# 4   Senky   28      Tokio
# 5  Tester   20  Testoland


print(dd)
# name            [Rent, Raya, Haos, Zero, Senky, Tester]
# age                            [20, 19, 19, 60, 28, 20]
# city    [Shiner, Poema, Poema, Swamp, Tokio, Testoland]
# dtype: object

del dd

print(df["name"]) # так же можно фильтровать постолбам
# 0      Rent
# 1      Raya
# 2      Haos
# 3      Zero
# 4     Senky
# 5    Tester
# Name: name, dtype: str

print(df.loc[1]) # это выводит имено по индексу
# name     Raya
# age        19
# city    Poema
# Name: 1, dtype: object


print(df[df["age"]>=20]) # так же можно выводить по условию
#      name  age       city
# 0    Rent   20     Shiner
# 3    Zero   60      Swamp
# 4   Senky   28      Tokio
# 5  Tester   20  Testoland



print(f'''

{df.head()}

{df.tail()}

{df.describe()}

{df.info()}
''')


# head() возвращает первые 5 строк таблицы
# #     name  age    city
# 0   Rent   20  Shiner
# 1   Raya   19   Poema
# 2   Haos   19   Poema
# 3   Zero   60   Swamp
# 4  Senky   28   Tokio


# tail() возвращает последние 5 строк таблицы
#      name  age       city
# 1    Raya   19      Poema
# 2    Haos   19      Poema
# 3    Zero   60      Swamp
# 4   Senky   28      Tokio
# 5  Tester   20  Testoland


# describe()  показывает статистику по числовым колонкам
#              age
# count   6.000000  сколько значений
# mean   27.666667  среднее арефметическое
# std    16.206994  стандартное отклонение
# min    19.000000  минимальное значение
# 25%    19.250000  25-й процентиль
# 50%    20.000000  медиана, середина значений: 20
# 75%    26.000000  75-й процентиль
# max    60.000000  максимальное значение


# info() показывает техническую информацию о таблице
# - сколько строк
# - сколько колонок
# - названия колонок
# - сколько непустых значений
# - типы данных
# - сколько памяти занимает DataFrame
#
# Примерно вывод будет такой:
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 6 entries, 0 to 5
# Data columns (total 3 columns):
#  #   Column  Non-Null Count  Dtype
#  0   name    6 non-null      object
#  1   age     6 non-null      int64
#  2   city    6 non-null      object
# dtypes: int64(1), object(2)
# memory usage: ...
# Главное:
# name — текст, поэтому object
# age — число, поэтому int64
# city — текст, поэтому object
# non-null значит “не пустое значение”.



# cv = pnd.read_clipboard() копирует то что в памети сохранено только текст
# cv = pnd.read_excel() читает exel файл
# cv = pnd.read_sql() читает sql файл
cv = pnd.read_csv('data.csv') #читает csv файл
print(cv.head())
#          Date  Platform   Views  Revenue
# 0  2023-01-01   YouTube  1000.0    500.0
# 1  2023-01-02   YouTube  1500.0    750.0
# 2  2023-01-03  Facebook  1200.0    600.0
# 3  2023-01-04   YouTube  1800.0    900.0
# 4  2023-01-05  Facebook  1100.0    550.0

filtered_cv = cv[cv["Platform"] == "YouTube"]
print(filtered_cv)
#          Date Platform   Views  Revenue
# 0  2023-01-01  YouTube  1000.0    500.0
# 1  2023-01-02  YouTube  1500.0    750.0
# 3  2023-01-04  YouTube  1800.0    900.0
# 5  2023-01-06  YouTube     NaN      NaN
# 9  2023-01-10  YouTube  1600.0    800.0


filtered_cv.to_csv('yt.csv', index=False) # сохраняет в csv файл без индексов



df.fillna(0, inplace=True) # ставит в пустные значения 0
df.dropna(inplace=True) # удаляет строки столбы с пустыми значениями
df.drop_duplicates(inplace=True) # удаляет дубликаты


df["age"] = df["age"].astype(int) # утверждаем что этот столб будет числом

grouped = df.groupby('age').sum()
print(grouped)
#            name             city
# age
# 19     RayaHaos       PoemaPoema
# 20   RentTester  ShinerTestoland
# 28        Senky            Tokio
# 60         Zero            Swamp
