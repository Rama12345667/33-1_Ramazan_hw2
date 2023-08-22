flags = {
    'kg': {'red', 'yellow'},
    'ru': {'white', 'blue', 'red'},
    'kz': {'blue', 'yellow'},
    'us': {'red', 'white', 'blue'},
    'tr': {'red', 'white'}
}

while True:
    colors = input("Введите цвет(а) через пробел (или 'q' для завершения): ")

    if colors.lower() == 'q':
        break

    input_colors = set(colors.split())
    matching_domains = []

    for domain, flag_colors in flags.items():
        if input_colors.issubset(flag_colors):
            matching_domains.append(domain)

    if matching_domains:
        print(', '.join(matching_domains))
    else:
        print("Нет стран с указанными цветами.")








