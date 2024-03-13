# Задание 1
from scipy import stats

dist_normal = stats.norm(loc=0, scale=1)
pdf_value_normal = dist_normal.pdf(0)
cdf_value_normal = dist_normal.cdf(0)
random_values_normal = dist_normal.rvs(size=10)

dist_uniform = stats.uniform(loc=-1, scale=2)  # Uniform(-1, 1) эквивалентно loc=-1, scale=2
pdf_value_uniform = dist_uniform.pdf(0)
cdf_value_uniform = dist_uniform.cdf(0)
random_values_uniform = dist_uniform.rvs(size=10)

print(" Нормальное распределение:")
print("   - Создание объекта распределения: dist_normal = stats.norm(loc=0, scale=1)")
print("   - Получение значения функции плотности вероятности: pdf_value_normal =", pdf_value_normal)
print("   - Получение значения функции распределения: cdf_value_normal =", cdf_value_normal)
print("   - Генерация случайных чисел из распределения: random_values_normal =", random_values_normal)

print(" Равномерное распределение:")
print("   - Создание объекта распределения: dist_uniform = stats.uniform(loc=-1, scale=2)")
print("   - Получение значения функции плотности вероятности: pdf_value_uniform =", pdf_value_uniform)
print("   - Получение значения функции распределения: cdf_value_uniform =", cdf_value_uniform)
print("   - Генерация случайных чисел из распределения: random_values_uniform =", random_values_uniform)

# Задание 2
from scipy import stats

sample_uniform = stats.uniform.rvs(loc=-1, scale=2, size=10)

t_statistic_1samp, p_value_1samp = stats.ttest_1samp(sample_uniform, popmean=0)

sample1 = [1, 2, 3, 4, 5]
sample2 = [6, 7, 8, 9, 10]
t_statistic_ind, p_value_ind = stats.ttest_ind(sample1, sample2)

print("Sample для одновыборочного t-теста:", sample_uniform)
print("t_statistic для одновыборочного t-теста, P_value для одновыборочного t-теста:", t_statistic_1samp, p_value_1samp)
print("Sample 1 для двухвыборочного t-теста:", sample1)
print("Sample 2 для двухвыборочного t-теста:", sample2)
print("t_statistic для двухвыборочного t-теста, P_value для двухвыборочного t-теста:", t_statistic_ind, p_value_ind)

