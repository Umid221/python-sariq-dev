mahsulotlar = ['un', "yog'", "go'sht", 'pomidor', 'bodring', 'ichimlik', 'don', 'kasha', 'shirinlik', 'meva']
savat =[]
for i in range(1, 6):
    savat.append(input(f'Savatga {i}-mahsulotni qo\'shing: '))

bor_mahsulotlar =[]
mavjud_emas =[]

for sav in savat:
    if sav in mahsulotlar:
        bor_mahsulotlar.append(sav)
    else:
        mavjud_emas.append(sav)

if mavjud_emas:
    print("Quyidagi mahsulotlar do'konimizda yo'q:")
    for item in mavjud_emas:
        print(item)
else:
    print("Siz so'ragan barcha mahsulotlar do'konimizda bor")