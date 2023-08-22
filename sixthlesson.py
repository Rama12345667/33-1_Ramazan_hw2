
# Шаг 1: Создать список ten, состоящий из целых чисел от 1 до 10
ten = list(range(1, 11))

# Шаг 2: Создать список evens, который состоит из четных чисел списка ten
evens = list(filter(lambda x: x % 2 == 0, ten))

# Шаг 3: Вывести на экран список возведенных в квадрат чисел от списка evens
squared_evens = list(map(lambda x: x ** 2, evens))
print(squared_evens)

# Шаг 4: Создать функцию для вывода объекта списка по указанному индексу
def print_item_by_index(index, my_list=ten):
    try:
        print(my_list[index])
    except IndexError:
        print(f"Индекс {index} недопустим. Введите индекс из диапазона 0-{len(my_list)-1}")

# Шаг 5: Бесконечный цикл запроса индекса и вывод элемента по индексу
while True:
    index_input = input("Введите индекс элемента для вывода (q для выхода): ")
    if index_input.lower() == 'q':
        break
    try:
        index = int(index_input)
        print_item_by_index(index)
    except ValueError:
        print("Неверный ввод индекса. Введите целое число.")

