son = int(input('juft son kiriting: '))
if son % 2 == 0:
    print('rahmat')
else:
    print('bu son juft emas')    

yosh = int(input('yoshingizni kiriting: '))
narx = 'chipta narxi'
if yosh <= 4 or yosh >= 60:
    print(f'{narx} bepul')
elif yosh <= 18:
    print(f'{narx} 10000 so\'m')
else:
    print(f'{narx} 20000 so\'m')

a = float(input('birinchi sonni kiriting: '))
b = float(input('ikkinchi sonni kiriting: '))
if a > b:
    print(f'{a} > {b}')
elif a == b:
    print(f'{a} = {b}')
else:
    print(f'{a} < {b}')

foydalanuvchilar = ['umid', 'ali', 'vali', 'umar', 'anvar']
foydalanuvchi = input('yangi login tanlang: ')
if foydalanuvchi not in foydalanuvchilar:
    print(f'Zush kelibsiz, {foydalanuvchi.title()}!')
else:
    print('Login band, yangi login tanlang')