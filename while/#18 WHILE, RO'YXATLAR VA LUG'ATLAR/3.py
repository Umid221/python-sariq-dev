print('mahsulotlaringizni kiriting')
mahsulotlar1 = []
n = 1
while True:
    mahsulot = input(f"{n}-mahsulotni kiriting: ")
    mahsulotlar1.append(mahsulot)
    a = input("yana mahsulot kiritasizmi?(ha/yo'q) ")
    if a == 'ha':
        n+=1
        continue
    else:
        break

print("Mahsulot va uning narxini kiriting")
mahsulotlar2 = {}
while True:
    mahsulot = input("Mahsulot nomini kiriting: ")
    narx = float(input(f"{mahsulot.title()} narxini kiriting: "))
    mahsulotlar2[mahsulot] = narx
    javob = input("yana mahsulot qo'shasizmi?(ha/yo'q) ")
    if javob != 'ha':
        break

for m in mahsulotlar1:
    if m in mahsulotlar2:
        print(m, mahsulotlar2[m], "so'm")
    else:
        print(f"Bizda {m} yo'q")