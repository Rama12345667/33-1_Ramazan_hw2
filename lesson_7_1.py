# lambda функция, работа с исключениями.
# lambda arguments: expression
# try:
#     code
# except:
#     code
#     message
# finally:
#     message
#     code

from random import choice
students_list = [9, 12, 13, 1, 3, 11, 6]
group_33_1 = {}
while students_list:
    print(f'next: {students_list}')
    chosen_student = choice(students_list)
    name = input(f'enter name for {chosen_student}: ').title()
    score = int(input(f'enter rate for {name}: '))
    group_33_1[name] = score
    students_list.remove(chosen_student)
    for n, r in group_33_1.items():
        print(f'{n}: {r}')

print(sum(group_33_1.values()) / len(group_33_1))

# word = 'python'
#
# while True:
#     try:
#         input_index = int(input('enter index: '))
#         print(word[input_index])
#     except Exception as info:
#         print("пишите числа от 0 до 5", info)

    # except IndexError:
    #     print('пишите числа от 0 до 5')
    # except ValueError:
    #     print('не надо писать буквы!')





# print(type(lambda_func))
# print(type(def_func))

# try:
#     print('3' + "5")
# except:
#     print('3 это строка а не числа')
# finally:
#     print("завершена проверка")

# print(int('python'))
# print({1:2, 5:6}[2])
# print(name)
# print('123'[8])







# pifagor = lambda num: [i * num for i in range(1, 10)]
# print(pifagor(int(input('enter num: '))))

# while True:
#     num1 = int(input('num 1: '))
#     symbol = input('enter + - / *')
#     num2 = int(input('num 2: '))
#     if symbol == '+':
#         res = lambda n1, n2: n1 + n2
#         print(res(num1, num2))


# new = lambda word='hello': word == word[::-1]
# print(new())

# map, filter
# numbers = list(range(1, 16))
# print(numbers)
#
# mapped = tuple(map(lambda num: num - 3, numbers))
# print(mapped)

# filtered = list(filter(lambda num: num > 9, numbers))
# print(filtered)

# lambda_func = lambda a, b: a + b
#
#
# def def_func(a, b):
#     return a + b
#
#
# print(lambda_func(5, 2))
# print(def_func(2, 5))

# def up_letter(word: str) -> str:
#     return word.title()
#
#
# def show_words(func, words):
#     for i in words:
#         print(func(i))

# show_words(lambda word: word.title(), ['rain', 'winter', 'autumn'])
# show_words(up_letter, ['osh', 'naryn', 'batken'])
# show_words(len, ['kg', 'bishkek', 'geeks'])
# show_words(str.upper, ['tokmok', 'karakol', 'kant'])
#
# attempts = 5
#
# while attempts > 0:
#     temperature = input(f'enter temperature: (or "stop") [{attempts}]')
#
#     if temperature == 'stop':
#         break
#     try:
#         temperature = int(temperature)
#         if temperature >= -40 and temperature <= 0:
#             print('холодно')
#         elif temperature >= 1 and temperature <= 10:
#             print('прохладно')
#         elif temperature >= 11 and temperature <= 25:
#             print('тепло')
#         elif temperature >= 26 and temperature <= 39:
#             print('жарко')
#         else:
#             print("невозможная температура!")
#         attempts -= 1
#     except:
#         print('введите температуру цифрами!')
#     finally:
#         print("проверка завершена")