rus = "ЁёЙйЦцУуКкЕеНнГгШшЩщЗзХхЪъФфЫыВвАаПпРрОоЛлДдЖжЭэЯяЧчСсМмИиТтЬьБбЮю"
eng = "~`QqWwEeRrTtYyUuIiOoPp[[]]AaSsDdFfGgHhJjKkLl;;''ZzXxCcVvBbNnMm,,../"
rus = rus.lower()
eng = eng.lower()
while True:
    word = input("Ваедите слово (для выхода нажмите 'q'): ")
    word = word.lower()
    if word == "q":
        print("Вы завешили программу")
        break
    for i in word:
        if i in eng:
            print(rus[eng.index(i)], end='')
        else:
            print(eng[rus.index(i)], end='')
