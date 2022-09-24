# Задача 43: Дана последовательность чисел.
# Получить список уникальных элементов заданной последовательности.

# Пример:

# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

some_list = [1, 2, 3, 5, 1, 5, 3, 10]

def remove_repeated(my_list):
    answer = {}
    for i in my_list:
        answer[i] = answer.get(i, 0) + 1
    unique_list = []
    for i in answer:
        if answer[i] == 1:
            unique_list.append(i)
    return unique_list

print(some_list)
print(remove_repeated(some_list))