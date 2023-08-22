# # Структуры данных: словари - dict, множества - set.
# # {key: value}
# print(type(numbers2))

menu = {
    'plov': {'rice', 'meat', 'carrot'},
    'beshbarmak': {'meat', 'noodles', 'potato'}
}

"""
        ЗАДАНИЕ

написать программу, которая просит ввести название блюда,
затем выдаёт ингридиенты указанного блюда, если оно есть!

использовать цикл while для повторного запроса ввода!

"""




# print({8, 3}.issubset([3, 8, 4]))
# while True:
#     time = input('enter time: ').lower()
#     if time == 'q':
#         break
#     if set('morning').issubset(time) or time == 'утро':
#         print('good morning')
#     elif time == 'day' or time == 'день':
#         print('good afternoon')
#     elif time == 'evening' or time == 'вечер':
#         print('good evening')
#     else:
#         print('hello')


plov = {'rice', 'meat', 'carrot'}
beshbarmak = {'meat', 'noodles', 'potato'}

print(plov.union(beshbarmak))
print(plov | beshbarmak)

print(plov.difference(beshbarmak))
print(plov - beshbarmak)

print(plov.intersection(beshbarmak))
print(plov & beshbarmak)

print(plov.symmetric_difference(beshbarmak))
print(plov ^ beshbarmak)

# numbers = [1, 2, 3, 1, 4, 5, 3]
# numbers2 = {1, 2, 3, 1, 4, 5, 3}
#
# print(numbers)
# print(numbers2)



# # print(type(student))
#
# # print(dict(enumerate('geeks')))
# # print(dict([['bir', 1], ['eki', 2], ['üch', 3]]))
# new = dict(name='Sam', age=22, country='UK')
# # print(new)
#
# student = {
#     'name': 'Jessica',
#     'age': 21,
#     'weight': 45.5,
#     'married': False,
#     'education': ('school', 'college'),
#     'pets': ['dog', 'cat', 'bird'],
#     'parents': {'father': 'Peter Parker', 'mather': 'Mary Jane'},
# }
#
# print(student.keys())
# print(student.values())
# print(student.items())
#
# for key, value in student.items():
#     print(f'{key} => {value}')
#
# # for i in student:
# #     print(i, ':', student[i])
#
# # print(student.get('name', 'нет такого ключа'))
# # print(student['nam'])
#
# '''add'''
# # student['hairs_color'] = 'red'
# # student['pets'].append('fish')
# # update посмотреть дома
#
# '''edit'''
# # student['weight'] += 1.3
# # student['age'] += 1
# # student['married'] = True
# # student['education'] = list(student['education'])
# # student['education'].append('bachelor')
# # student['education'] = tuple(student['education'])
#
# '''delete'''
# # student['age'] = None
# # del student['pets'][-1]
# # student['pets'].remove('cat')
# # del student['age']
# # student.pop('pets')
#
# # print(student)
#
# # print(student['name'])
