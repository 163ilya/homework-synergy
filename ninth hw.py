# Задание 1

def nod(x, y):
    while y:
        x, y = y, x % y
    return x

def nok(a, b):
    return abs(a * b) // nod(a, b)

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

result = nok(a, b)
print(f"Наименьшее общее кратное чисел {a} и {b} равно {result}.")


# Задание 2

def find_simple(n):
    simple = []
    for i in range(2, n + 1):
        is_simple = True
        for delit in range(2, int(i**0.5) + 1):
            if i % delit == 0:
                is_simple = False
                break
        if is_simple:
            simple.append(i)
    return simple

n = int(input("Введите число n: "))

simple_numbers = find_simple(n)
print(f"Простые числа от 1 до {n}: {simple_numbers}")


# Задание 3

def find_delit(n):
    delit = [i for i in range(1, n + 1) if n % i == 0]
    return delit

n = int(input("Введите число n: "))

delit = find_delit(n)
print(f"Делители числа {n}: {delit}")

