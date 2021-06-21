b_son = int(input('istalgan butun son kiriting: '))

boluvchilar = []

for i in range(2, 11):
    if b_son % i == 0:
        boluvchilar.append(i)

for son in boluvchilar:
    print(f'{b_son} soni {son}ga qoldiqsiz bo\'linadi')