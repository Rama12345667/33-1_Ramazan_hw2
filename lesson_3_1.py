# Циклы
# [start:stop:step]
# print(len(word))
# i - iterable, item

eng = 'qwerty'
rus = 'йцукен'


print(eng[rus.index('й')])

# print('geeks'.index('e', 2))

# fknиул
# ghjuhfvvbhjdfybt d ,birtrt
# зкщпкфььштп шт ишырлул




# cash = 1000
# percents = 0.1
# years = 5
#
# for year in range(1, years+1):
#     cash += cash * percents
#     print(f'{year} - {cash}')


# for i in range(1, 4):
#     for j in range(1, 4):
#         print(i, j)

# for number in range(1, 6):
#     print(number)

# word = 'satisfaction'
#
# for letter in word:
#     if letter == 'c':
#         break
#     print(letter, end='')

# print('2345345'.isnumeric())
# print('fghFrfg'.startswith('t'))
# print('fghFrfg'.endswith('g'))

# word = 'programming'
# c = -1
# while c < len(word):
#     c += 1
#     if word[c] in 'rm':
#         continue
#     print(word[c], end=' ')

# print(word[::-1])
# print(word[::4])
# print(word[3:7])

# print(word[0])
# print(word[3])
# print(word[-2])

# attempts = 10
#
# while attempts > 0:
#     temperature = input('enter temp: ')
#     if temperature == 'stop':
#         print('exit...')
#         break
#     temperature = int(temperature)
#     if temperature >= -40 and temperature <= 5:
#         print('холодно')
#     elif temperature >= 6 and temperature <= 15:
#         print('прохладно')
#     elif temperature >= 16 and temperature <= 25:
#         print('тепло')
#     elif temperature >= 26 and temperature <= 40:
#         print('жарко')
#     else:
#         print('невозможная температура!')
#     attempts -= 1

# n = 5
#
# while n > 0:
#     print(n)
#     n -= 1

# c = 0
#
# while True:
#     print('hello', c)
#     c += 1
#     if c == 50:
#         break
