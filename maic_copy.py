import pandas as pd
import numpy as np
from pandas import DataFrame as df
print('Перемести ваш файл с имеющимися заголовками в директорию с проектом')
print('Пример входящего файла, количество столбцов и строк может быть любым(файл primer.csv в директории проекта)')
b = pd.read_csv('primer.csv', delimiter=',')
b = pd.DataFrame(b)
print(b,'\r\n')
print('Введите название файла, например file.csv(только csv файлы)')
name_file=input()
a = pd.read_csv(name_file, delimiter=',')
df2 = pd.DataFrame(a)
df2_1=df.sort_index(df2,axis=1, ascending=False)
print(df2_1,)
print('\r\nВведите названия столбца по которому произойдёт фильтрация.\r\nПроизойдёт '
      'группировка и суммирование по этому значению')
filtr_stolbec=input()
df3= df.groupby(df2, by=filtr_stolbec).sum()
print(df3)

input()


##Блок кода для ручного ввода таблицы
#import pandas as pd
#import numpy as np
#from pandas import DataFrame as df
##Водить сюда в том же формате^^
#df2= pd.DataFrame({'tovar':['banan','hleb','banan','hleb'],'count':[11,12,13,14],'date':['2022-03-07', '2022-03-07', '2022-03-08','2022-03-08']})
##Водить сюда в том же формате^^
##Значение перед квадратными скобками - имя столбца по которому будет отрабатывать фильтрация из блока ниже
#df2_1=df.sort_index(df2,axis=1, ascending=False)
#print(df2_1,)
#print('\r\nВведите названия столбца по которому произойдёт фильтрация.\r\nПроизойдёт'
#      'группировка и суммирование по этому значению')
#filtr_stolbec=input()
#df3= df.groupby(df2, by=filtr_stolbec).sum()
#print(df3)