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

# задача 6

s = input("Введите строку: ")

line=""
k=0
for i in s:
   if (i=="("):
       k=1
   if (k==1):
       line=line+i
   if (i==")"):
       k=0
def find_substring(s, left_bracket, right_bracket):
    left_bracket_index = s.find(left_bracket)
    right_bracket_index = s.find(right_bracket, left_bracket_index + 1)
    substring = s[left_bracket_index + 1: right_bracket_index]
    return substring
substring = find_substring(s, '(', ')')
print (f" {substring}")
