day = int(input("Введите ваш день рождения: "))
month = int(input("Введите ваш месяц рождения: "))
while True:
 if month == 3 and day >=21 and day <=31:
    print("Овен")
 elif month == 4 and day <= 20 and day >=1:
    print("Овен")

 elif month == 4 and day >=21 and day <= 30:
    print("Телец")
 elif month == 5 and day >= 1 and day <=21:
    print("Телец")

 elif month == 5 and day >=22 and day <=31:
    print("Близднецы")
 elif month == 6 and day >= 1 and day <= 21:
    print("Близднецы")

 elif month == 6 and day >=22 and day <=30:
    print("Рак")
 elif month == 7 and day >= 1 and day <= 22:
    print("Рак")

 elif month == 7 and day >=23 and day <=31:
    print("Лев")
 elif month == 8 and day >= 1 and day <= 21:
    print("Лев")

 elif month == 8 and day >=22 and day <=31:
    print("Дева")
 elif month == 9 and day >= 1 and day <= 23:
    print("Дева")

 elif month == 9 and day >=24 and day <=30:
    print("Весы")
 elif month == 10 and day >= 1 and day <= 23:
    print("Весы")

 elif month == 10  and day >=24 and day <=31:
    print("Скорпион")
 elif month == 11  and day >= 1 and day <= 22:
    print("Скорпион")

 elif month == 11  and day >=23 and day <=30:
    print("Стрелец")
 elif month == 12  and day >= 1 and day <= 22:
    print("Стрелец")

 elif month == 12  and day >=23 and day <=31:
    print("Козерог")
 elif month == 1  and day >= 1 and day <= 20:
    print("Козерог")

 elif month == 1  and day >=21 and day <=31:
    print("Водолей")
 elif month == 2  and day >= 1 and day <= 19:
    print("Водолей")

 elif month == 2 and day >= 20 and day <= 29:
    print("Рыбы")
 elif month == 3 and day >= 1 and day <= 20:
     print("Рыбы")

 else:
    print("Вы ввели данные неправильно")


