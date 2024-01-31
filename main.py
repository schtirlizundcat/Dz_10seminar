# Для пересортировки в случайном порядке
import random
# для работы с dataframe
import pandas as pd
# Для вывода dataframe в консоль в текстово-табличном виде
from tabulate import tabulate

# Метод для преобразования dataframe в вид one-hot относительно заданного столбца
def one_hot_encode(df, one_hot_column):
    unique_values = df.iloc[:, one_hot_column].unique()
    for value in unique_values:
        df[value] = (df.iloc[:, one_hot_column] == value).astype(int)
    df.drop(df.columns[one_hot_column], axis=1, inplace=True)

# Задаём массив
lst = ['robot'] * 10
lst += ['human'] * 10
# «Тусуем» в случайном порядке с использованием random.shuffle()
random.shuffle(lst)

# Создаём DataFrame data на основе массива lst
data = pd.DataFrame({'whoAmI':lst})
# Проверим полученный DataFrame
data.head()

# Переводим data в вид one hot
one_hot_encode(data, 0)

# Выводим результат на stdout в виде простой текстовой (псевдографической) таблицы
print(tabulate(data, headers='keys', tablefmt='psql'))