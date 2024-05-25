"""
2. Задайте переменные разных типов данных:
  - Создайте переменную immutable_var и присвойте ей кортеж из нескольких элементов разных типов данных.
  - Выполните операции вывода кортежа immutable_var на экран.

3. Изменение значений переменных:
  - Попытайтесь изменить элементы кортежа immutable_var. Объясните, почему нельзя изменить значения элементов кортежа.

4. Создание изменяемых структур данных:
  - Создайте переменную mutable_list и присвойте ей список из нескольких элементов.
  - Измените элементы списка mutable_list.
  - Выведите на экран измененный список mutable_list.
"""

immutable_var = (1, 1.34, True, [1, 2, 3], 'apple', (1, 2, 3))
print('Immutable tuple:', immutable_var)

# immutable_var[2] = False    => такая операция невозможна, получим ошибку
# immutable_var[3] = False    => такая операция невозможна, получим ошибку
# поскольку "tuple" является неизменяемой упорядоченной коллекцией данных, то изменить по индексу
# содержащиеся в кортеже данные объекты нельзя.
# Однако, если кортеж содержит внутри себя изменяемые типы данных, то эти данные могут быть изменены.
immutable_var[3][0] = False  # => такая операция возможна,
# получим кортеж (1, 1.34, True, [False, 2, 3], 'apple', (1, 2, 3))

mutable_list = [1, 1.34, True, [1, 2, 3], 'apple', (1, 2, 3)]
mutable_list[-1] = 'sun'
print('Mutable list:', mutable_list)
