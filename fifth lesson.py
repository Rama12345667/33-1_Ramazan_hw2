flags = {
    'kg': {'red', 'yellow'},
    'ru': {'white', 'blue', 'red'},
    'kz': {'blue', 'yellow'},
    'us': {'red', 'white', 'blue'},
    'tr': {'red', 'white'}
}

while True:
    colors = input("введите цвет: ")
    input_colors = set(colors.split())
    if colors.lower() == 'q':
        break
    sames = []

    for domain, flag_colors in flags.items():
        if input_colors.issubset(flag_colors):
            sames.append(domain)

    if sames:
        print(','.join(sames))
    else:
        print("нет такой страны с таким цыктом")


