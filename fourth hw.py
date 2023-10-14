# задача 1
text = "Death there mirth way the noisy merit"
a = text.split()
print(a[::-1])

# задача 2
a = "In the hole in the ground there lived a hobbit"
print(a[::2])

# задача 3
lst = [3, 5, -7, -13, 43, 8, 0, -13, 8, -1, 2]
lst2 = []
for i in lst:
    lst2.append(i**2)
print(lst2)

# задача 4
text = input("Введите текст ")
a = input("Введите символ ")
print(text.replace(a, a * 2))

# задача 5
string = input()
x = "x"
КоличествоX = string.count(x)
y = "y"
КоличествоY = string.count(y)
result = f"x: {КоличествоX}, y: {КоличествоY}"
print(result)

# задача 6 - решил странно, понятно только так
# если есть подсказка как использовать find, прикрепите пожалуйства
text = "When he saw Sally (a girl he used to go to school with) in the shop, he could not believe his eyes. She was fantastic (as always)!"
text.find("(a girl he used to go to school with)" and "(as always)")
print("a girl he used to go to school with")
print("as always")
