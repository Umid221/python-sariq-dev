mahsulotlar = ['un', "yog'", "go'sht", 'pomidor', 'bodring', 'ichimlik', 'don', 'kasha', 'shirinlik', 'meva']

savat =[]
for i in range(1, 6):
    savat.append(input(f'Savatga {i}-mahsulotni qo\'shing: '))

for s in savat:
    if s in mahsulotlar:
        print(f"Do'konimizda {s} bor")
    else:
        print(f"Do'konimizda {s} yo'q")