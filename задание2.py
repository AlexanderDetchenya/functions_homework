# Создайте программу, которая, принимая массив имён, возвращает строку описывающая количество
# лайков (как в Facebook).

def likes():
    names_sp = []
    for i in range(20):
        name = input('Vvedite imya layknuvshego("n" - vse perechisleni): ')
        if name != 'n':
            names_sp.append(name)
        if name == 'n':
            break
    if len(names_sp) == 0:
        print('no likes')
    elif len(names_sp) == 1:
        print(names_sp[0], 'likes this')
    elif len(names_sp) == 2:
        print(names_sp[0], 'and', names_sp[1], "like this")
    elif len(names_sp) == 3:
        print(names_sp[0], names_sp[1], 'and', names_sp[2], "like this")
    elif len(names_sp) >= 4:
        print(names_sp[0], names_sp[1], 'and', len(names_sp)-2, "others like this")

likes()



