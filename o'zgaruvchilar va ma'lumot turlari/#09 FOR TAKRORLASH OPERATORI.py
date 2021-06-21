ismlar =['ali', 'vali', 'salim', 'halim', 'karim']

for n in ismlar:
    print(f'salom {n}')
print(f'kod {len(ismlar)} marta takrorlandi')

toqlar = list(range(11, 100, 2))
for a in toqlar:
    print(a**3)

kinolar=[]
print('5 ta yaxshi ko\'rgan kinongiz nomini kiriting')
for k in range(5):
    kinolar.append(input())
print(kinolar)

son = int(input('bugun necha kishi bilan suhbat qildingiz? >>> '))
for u in range(son):
    input(f'{u+1}-suhbat qilgan odamingiz kim edi: ')
