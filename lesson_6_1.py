# Функции, аргументы: *args, **kwargs.
# DRY - don't repeat yourself
# def - define
"""схема функции"""

# def menu(**kwargs):
#     return kwargs
#
# monday = menu(drink='tea', eat='pizza', dfg=True, rth=123)
# print(monday)

# def plus(*args):
#     print(args)
#     return sum(args)
#
# print(plus(2, 4, 3, 7, 45, 12, 234))


# определение наименование(параметры):
#     тело функции
#     возврат
# наименование(аргументы)

word = input('enter word: ')
counter = 0
for _ in word:
    counter += 1
print(counter)

def len1(sequence):
    counter = 0
    for _ in sequence:
        counter += 1
    return counter

print(len1(''))
print(len([2, 3, 4, 5]))

# print(min([2, 3, 4, 5]))

# print(max([2, 3, 4, 5]))

# print(sum([2, 3, 4, 5]))


# def greet(name, surname="Неизвестно"):  # обязательный позиционный параметр
#     print(f'name: {name} surname: {surname}')
#
# greet("Азамат", 'Адылбеков')  # обязательный позиционный аргумент
# greet("Алина", "Баженова")
# greet(surname='lee', name='bruce')  # именованные аргументы

def get_square(length: int, width: int) -> int:
    """
    Принимает длину и ширину, возвращает площадь!
    """
    return length * width


square_2 = get_square(8, 5)
square_hall = get_square(length=18, width=12)
# print(square_2, square_hall, sep='\n')
# print((square_2 + square_hall))

# print(get_square.__doc__)
# print(help(get_square))

# print(len.__doc__)
# print(help(len))

# length = 8
# width = 5
# square_2 = length * width
# print(square_2)
#
# length = 18
# width = 12
# square_hall = length * width
# print(square_hall)
