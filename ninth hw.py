# Задание 1

def find_nod(x, y):
    while y:
        x, y = y, x % y
    return x

def find_nok(a, b):
    return abs(a * b) / find_nod(a, b)

# Ввод двух чисел от пользователя
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

# Находим и выводим НОК
lcm = find_nok(a, b)
print("Наименьшее общее кратное чисел", a, "и", b, "равно", int(lcm))


# Задание 2

def prostoe(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_prostoe(n):
    primes = [num for num in range(2, n + 1) if prostoe(num)]
    return primes

# Ввод числа n от пользователя
n = int(input("Введите число n: "))

# Находим и выводим простые числа от 1 до n
prime_numbers = find_prostoe(n)
print(f"Простые числа от 1 до {n}: {prime_numbers}")



# Задание 3

def find_split(n):
    split = []
    for i in range(1, n + 1):
        if n % i == 0:
            split.append(i)
    return split

n = int(input("Введите число n: "))

split_list = find_split(n)
print("Делители числа {}: {}".format(n, split_list))




