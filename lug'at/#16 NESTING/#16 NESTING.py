shaxslar = [
    {'ism':'AL-Buxoriy', 'ty':810, 'manzil':'Buxoro', 'umr':60, 'asarlar':['al-jome\' as-sahih', 'al-adab al-mufrad', 'attarixul kabir', 'attarixus sag\'ir']},
    {'ism':'Abdulla Qodiriy', 'ty':1894, 'manzil':'toshkent', 'umr':44, 'asarlar':["o'tgan kunlar", 'mehrobdan chayon', 'obid ketmon']},
    {'ism':'erkin vohidov', 'ty':1936, 'manzil':'Farg\'ona', 'umr':80, 'asarlar':['tong nafasi', "qo'shiqlarim sizga", "o'zbegim"]},
    {'ism':'Alisher navoiy', 'ty':1441, 'manzil':'Hirot', 'umr':60, 'asarlar':['xamsa', 'lison ut-tayr', 'munojot']}
]
for shaxs in shaxslar:
    print(f"{shaxs['ism'].title()} {shaxs['ty']}-yilda {shaxs['manzil'].title()}da tavallud topgan. {shaxs['umr']} yil umr ko'rgan.")
print()
for shaxs in shaxslar:
    print(f"{shaxs['ism']}ning mashhur asarlari:")
    for asar in shaxs['asarlar']:
        print(asar.capitalize())
    print()