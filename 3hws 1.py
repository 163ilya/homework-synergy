
# Задание 1

from scipy import stats

dist = stats.norm(loc=0, scale=1)

pdf_value = dist.pdf(0)
cdf_value = dist.cdf(0)

random_values = dist.rvs(size=10)

print(" Нормальное распределение:")
print("   - Создание объекта распределения: dist = stats.norm(loc=0, scale=1)")
print("   - Получение значения функции плотности вероятности: pdf_value =", pdf_value)
print("   - Получение значения функции распределения: cdf_value =", cdf_value)
print("   - Генерация случайных чисел из распределения: random_values =", random_values)

# Задание 2

from scipy import stats

sample = [1, 2, 3, 4, 5]
t_statistic_1samp, p_value_1samp = stats.ttest_1samp(sample, popmean=3)

sample1 = [1, 2, 3, 4, 5]
sample2 = [6, 7, 8, 9, 10]
t_statistic_ind, p_value_ind = stats.ttest_ind(sample1, sample2)


print("Sample для ttest_1samp:", sample)
print("t_statistic для ttest_1samp, P_value for ttest_1samp:", t_statistic_1samp, p_value_1samp)
print("Sample 1 для ttest_ind:", sample1)
print("Sample 2 для ttest_ind:", sample2)
print("t_statistic for ttest_ind, P_value for ttest_ind:", t_statistic_ind, p_value_ind)


