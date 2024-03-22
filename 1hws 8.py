def find_max_recursive(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        max_rest = find_max_recursive(lst[1:])
        return lst[0] if lst[0] > max_rest else max_rest

# Пример использования:
my_list = [3, 8, 1, 6, 2, 8, 10, 4]
max_number = find_max_recursive(my_list)
print("Максимальное число в списке:", max_number)
