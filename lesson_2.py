# time = input('eneter time: ').lower()
#
# if time == 'morning' or 'утро':
#     print('Good morning')
#
# elif time == 'day' or 'день':
#     print('good afternoon')
#
# elif time == 'evening ' or 'вечер':
#     print('good evening')
#
# else:
#     print('Hel

weather = float(input("temperature now - "))
if weather <= 15 and weather >= -20:
    print('cold')

elif weather >= 14  and  weather <= 27:
    print('warm')

elif weather >= 28 and weather <= 50:
    print('hot')

else:
    print('НЕ ВЫЖИВЕТ!')

