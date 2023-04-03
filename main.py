# Создание фуекции для пузырьковой сортировки
def bubble_sort(list1):
    # Внешний цикл для обхода всего списка
    for i in range(0, len(list1) - 1):
        for j in range(len(list1) - 1):
            if (list1[j] > list1[j + 1]):
                temp = list1[j]
                list1[j] = list1[j + 1]
                list1[j + 1] = temp
    return list1


list1 = [3, 7, 5, 1]
print("Неотсортированый список: ", list1)
# Вызов функции пузырьковой сортировки
print("Отсротированный список: ", bubble_sort(list1))
