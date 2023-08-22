# Структуры данных: списки - list, срезы, кортежи - tuple.
# print(type(objects))
# [object cycle condition]

# numbers = [3, 6, 8, 3]
objects = [3, 6, 8, 3, 5, 8, 9]

# numbers = tuple(numbers)
# print(numbers)

# new = ('56',)
# print(type(new))

# objects = (True, 56, 7.9, 'Python')
# print(type(objects))
# print(objects)

# numbers = list(range(1, 21))
# print(numbers)
# new = [num*5 for num in numbers if num > 9]
# new1 = [num*5 for num in numbers if num < 9]
# print(new)
# print(new1)

# holidays = ['sat', 'sun', 'january']
#
# found = [i for i in holidays if i in days]
# print(found)

# days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
# total_expenses = sum([int(input(f'{i.upper()}: ')) for i in days])
# # total_expenses = 0
# # for day in days:
# #     total_expenses += int(input(f'enter exp for {day.upper()}: '))
#
# print(
#     f'total: {total_expenses}\n'
#     f'average: {total_expenses / len(days)}'
# )


# word = 'python'
# word = list(word)
# numbers = list(range(1, 6))
# print(numbers)

# objects = [996, True, 6.3, 312, False, 5.5]
# new = objects.copy()
# new = objects[::]
#
# print(id(objects))
# print(id(new))
#
# print(objects == new)
# print(objects is new)
#
# print(objects)
# print(new)

'''delete'''
# objects.clear()
# del objects[2:5]
# objects.remove(996)
# deleted = objects.pop(3)
# print(deleted)

'''edit'''
# objects.reverse()
# objects = objects[::-1]
# objects.sort(reverse=True)
objects[1], objects[-3] = objects[-3], objects[1]
# objects[0] = 'day'

'''add'''
# objects.append('Python')
# objects.insert(4, 'water')
# objects.extend(numbers)
# objects += numbers

print(objects)