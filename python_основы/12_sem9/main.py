import pandas as pd

df = pd.read_csv('california_housing_test.csv')
print(df.tail())

print(df.head())

print(df.sample(10))

print("размеры файла")
print(df.shape)
print("Тип элементов в файле")
print(df.dtypes)

print("Общая информация о файле:")
print(df.info())

print("Описание данных:")
print(df.describe())

print("Проверяем на пустые значения")
print(df.isnull())
print("Или так: ")
print(df.isna())

print("Считаем пустые значения")
print(df.isnull().sum())

print("_" * 50)
# Показать median_house_value где median_income < 2
# Показать данные в первых 2 столбцах

print(df[df['median_income'] < 2]['median_house_value'])
print("_" * 50)
print("Или так: ")
print(df.loc[df['median_income'] < 2, 'median_house_value'])

print("выводим 2 первых столбца. топорный метод. ")
print(df[['longitude', 'latitude']])  # вместо столбца передаем лист, в котором указан нужные столбцы.
print("_" * 10)
print(df.columns)  # выводим названия колонок
print(df.columns[:2])
print(df[df.columns[:2]])

print("_" * 50)
print(df.iloc[:5, :2])  # Вводим 5 строк и 2 колонки. iloc работает с индексами
print("_" * 10)
print(df.loc[:, ['longitude', 'latitude']])  # loc работает с названиями столбцов.
print("_" * 10)
print(df.loc[:5, :'latitude'])  # В функции loc срезы работают включительно с последним элементом.

print("_" * 10)
print(df.loc[:4, df.columns[:2]])
print("_" * 10)
print(df.loc[:4, :df.columns[1]])

# Выбрать данные где housing_median_age < 20 и median_house_value > 70000
print("_" * 50)
print(df[(df['housing_median_age'] < 20) & (df['median_house_value'] > 70000)])

print("_" * 80)
# Задача №61. Определить какое максимальное и минимальное значение median_house_value
#
print(df['median_house_value'].min(), df['median_house_value'].max())

print("-" * 10)
# Показать максимальное median_house_value, где median_income = 3.1250
print(df[df['median_income'] == 3.1250]['median_house_value'].max())
print("-" * 10)
#
# Узнать какая максимальная population в зоне минимального значения median_house_value
print(
    df[
        df[
            'median_house_value'] == df['median_house_value'].min()
        ]['population'].max()
)

print(pd.set_option('display.max_rows', 50))
