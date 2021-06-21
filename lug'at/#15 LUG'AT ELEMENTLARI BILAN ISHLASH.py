python_izohli_lugati = {'integer':'butun son', 'float':'o\'nli son', 'string':'xarakterlar to\'plami', 'varieble':'o\'zgaruvchi', 'def':'formula boshlash uchun ishlatiladi', 'loop':'sikl', 'if':'agar', 'else':'aks holda', 'list':'ro\'yxat', 'tuple':'o\'zgarmaydigan ro\'yxat'}
for k, v in sorted(python_izohli_lugati.items()):
    print(f"{k} - {v}")
print('---------------------------------------')
davlatlar = {
    "o'zbekiston":'toshkent',
    'aqsh':'washington d.c.',
    'rossiya':'moskva',
    'tojikiston':'dushanbe',
    "qirg'iziston":'bishkek',
    'qozog\'iston':'nursulton',
    'malayziya':'kuala-lumpur',
    'singapur':'sungapur',
    'italiya':'rim'}
print("Dunyo davlatlari")
for a in sorted(davlatlar.keys()):
    print(a.upper())
print('---------------------------------------')
print("Davlatlarning poytaxti")
for b in sorted(davlatlar.values()):
    print(b.title())
print('---------------------------------------')
davlat = input('- Qaysi davlatning poytaxttini bilishni istaysiz?\n- ').lower()
poytaxt = davlatlar.get(davlat)
if poytaxt == None:
    print("Kechirasiz, bizda bu haqida ma'lumot yo'q")
else:
    print(f"{davlat.upper()}ning poytaxti {poytaxt.title()}")
print('---------------------------------------')
menu = {'osh':20000, 'sho\'rva':15000, 'manti':3000, "lag'mon":13000, 'somsa':5000, 'kabob':18000, 'shashlik':50000, 'jiz':100000, 'mastava':15000, 'ayron':5000}
print('3 ta taom buyurtma bering')
t1 = input('1-taom: ').lower()
t2 = input('2-taom: ').lower()
t3 = input('3-taom: ').lower()
taomlar = [t1, t2, t3]
for taom in taomlar:
    if taom in menu:
        print(f"{taom.title()} {menu[taom]} so'm")
    elif taom not in menu:
        print(f"Kechirasiz, bizda {taom} yo'q")