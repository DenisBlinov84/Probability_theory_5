# Проведите тест гипотезы. Продавец утверждает, что средний вес пачки печенья составляет 200 г.
# Из партии извлечена выборка из 10 пачек. Вес каждой пачки составляет:
# 202, 203, 199, 197, 195, 201, 200, 204, 194, 190.
# Известно, что их веса распределены нормально.
# Верно ли утверждение продавца, если учитывать, что доверительная вероятность равна 99%? (Провести двусторонний тест.)

import numpy as np
from scipy import stats

cookies=np.array([202, 203, 199, 197, 195, 201, 200, 204, 194, 190])

tn=(np.mean(cookies)-200)/(np.std(cookies,ddof=1)/len(cookies)**0.5)
print(f'Наблюдаемое значение t-критерия: {tn: .4f}')

# табличное значение t критерия a/2= 0.01/2 = 0.005

tt=stats.t.ppf(0.995,len(cookies)-1)
print(f'Табличное значение t-критерия: {tt: .4f}')

# Сравним полученные значения (поскольку у нас двусторонний критерий, то используем абсолютное значение полученного t-критерия):
print(np.abs(tn)<tt)

# Ответ:
# Принимаем нулевую гипотезу 


