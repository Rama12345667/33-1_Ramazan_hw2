ten = list(range(1, 11))

evens = list(filter(lambda x: x % 2 ==0, ten))

squared_evens = list(map(lambda x: x ** 2, evens))

print(squared_evens)


def indexter(index,my_list = ten):
    try:
        print(my_list[index])
    except IndexError:
        print(f"Индекс недопустим. Введите индекс из диапазона 0-{len(my_list) - 1}")

while True:
    index_input = input("Введите индекс для вывода ('q' для выхода): ")
    if index_input.lower() == 'q':
        break
    try:
        index = int(index_input)
        indexter(index)
    except ValueError:
        print("Неверный ввод индекса. Введите целое число.")


