print('mahsulotlaringizni kiriting')
mahsulotlar = []
n = 1
while True:
    mahsulot = input(f"{n}-mahsulotni kiriting: ")
    mahsulotlar.append(mahsulot)
    a = input("yana mahsulot kiritasizmi?(ha/yo'q) ")
    if a == 'ha':
        n+=1
        continue
    else:
        break