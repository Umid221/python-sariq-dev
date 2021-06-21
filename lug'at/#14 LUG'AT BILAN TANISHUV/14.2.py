python_izohli_lugati = {'integer':'butun son', 'float':'o\'nli son', 'string':'xarakterlar to\'plami', 'varieble':'o\'zgaruvchi', 'def':'formula boshlash uchun ishlatiladi', 'loop':'sikl', 'if':'agar', 'else':'aks holda', 'list':'ro\'yxat', 'tuple':'o\'zgarmaydigan ro\'yxat'}

a = input('biror kalit so\'z liriting: ').lower()

tarjima = python_izohli_lugati.get(a)
if tarjima == None:
    print('Bunday so\'z mavjud emas')
else:
    print(f"{a} so'zi {tarjima} deb tarjima qilinadi")