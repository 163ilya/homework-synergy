# задание 1
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

result = list(map(lambda x, y: x + y, list1, list2))

print(result)

# задание 2
numbers = [17, 19, 24, 39, 65, 78, 91, 104, 117, 133] # можно использовать и другие цифры

result = list(filter(lambda x: x % 19 == 0 or x % 13 == 0, numbers))

print(result)

# задание 3
from functools import reduce

numbers = [12, 34, 23, 45, 67, 89, 100, 56] # можно использовать и другие цифры

max_number = reduce(lambda x, y: x if x > y else y, numbers)

print(max_number)
