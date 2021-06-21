otam = {'ism':'Nurillo', 'yil':'1970', 'joy':'Kogon'}
print(f"Otamning ismlari {otam['ism']}, {otam['yil']}-yilda {otam['joy']}da tug\'ilganlar")

taomlar = {'ali':'manti', 'vali':'osh', 'soli':'mosh', 'anvar':'kabob', 'yunus':'qaymoq'}
print(f'Alining sevimli taomi {taomlar["ali"]}')
print(f'Valining sevimli taomi {taomlar["vali"]}')
print(f'Solining sevimli taomi {taomlar["soli"]}')

python_izohli_lugati = {'integer':'butun son', 'float':'o\'nli son', 'string':'xarakterlar to\'plami', 'varieble':'o\'zgaruvchi', 'def':'formula boshlash uchun ishlatiladi', 'loop':'sikl', 'if':'agar', 'else':'aks holda', 'list':'ro\'yxat', 'tuple':'o\'zgarmaydigan ro\'yxat'}

a = input('biror kalit so\'z liriting: ').lower()
print(python_izohli_lugati.get(a, 'bunday so\'z mavjud emas'))