cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car == 'gm':
        print(car.upper())
    else:
        print(car.title())

for car in cars:
    if car != 'gm':
        print(car.title())
    else:
        print(car.upper())

login = input('loginni kiriting: ')
if login.lower() == 'admin':
    print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
    print(f'Xush kelibsiz, {login}!')

a = input('son kiriting: ')
b = input('yana son kiriting: ') 
if a == b: print("Sonlar teng")

son = float(input('son kiriting: '))
if son < 0:
    print('manfiy son')
else: 
    print('musbat son')

son = float(input('son kiriting: '))
if son < 0:
    print('musbat son kiriting')
else: 
    print(son**(1/2))