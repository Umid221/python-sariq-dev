print("Mahsulot va uning narxini kiriting")
mahsulotlar = {}
while True:
    mahsulot = input("Mahsulot nomini kiriting: ")
    narx = float(input(f"{mahsulot.title()} narxini kiriting: "))
    mahsulotlar[mahsulot] = narx
    javob = input("yana mahsulot qo'shasizmi?(ha/yo'q) ")
    if javob != 'ha':
        break
print(mahsulotlar)