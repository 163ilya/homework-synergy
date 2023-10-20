# задание 1

def Palindrome_test_string(input_str):
    lower = input_str.lower()
    return lower == lower[::-1]

print(Palindrome_test_string('abccbA')) # можно ставить другие значения в ' '

# задание 2

a = input("Введите имя ")
b = input("Введите фамилию ")
c = input("Введите отчество ")

year = input("Введите год рождения ")

def print_fio(a, b, c, year):
   print(f"{b} {a} {c} {year} г.р. зарегестрирован")


print_fio(a, b, c, year)

# задание 3

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

print('Максимальным числом является: ', end='')

if b <= a >= c:
    print(a)
elif a <= b >= c:
    print(b)
elif a <= c >= b:
    print(c)
