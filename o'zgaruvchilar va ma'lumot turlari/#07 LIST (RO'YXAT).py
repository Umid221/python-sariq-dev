ismlar = ['eshmat', 'toshmat', 'hikmat']
print(f'1-sining ismi {ismlar[0].title()}, keyingisiniki {ismlar[1].capitalize()}, boshqasiniki {ismlar[2].title()}')

sonlar = [234,-345,5,4.4,234.4,-45.4]
print(sonlar[0] + sonlar[1] - sonlar[2] * sonlar[3] / sonlar[4])
sonlar[5] = 453.4
sonlar[4] = sonlar[2]*1.2
print(sonlar)

t_shaxslar = ['Amir Temur', 'Buxoriy', 'Termiziy']
z_shaxslar = ['Abdulloh', 'Elon Musk', 'Salah']
print('Men tarixiy shaxslardan', t_shaxslar[1],'bilan, zamonaviy shaxslardan esa', z_shaxslar[1], 'bilan suhbat qilishni istar edim')

friends = []
friends.append('ali')
friends.append('vali')
friends.append('sherali')
friends.append('muhammadali')
friends.append('salim')
friends.remove('vali')
friends.insert(0, 'rawad')
friends.insert(-1, 'jack')
friends.insert(3, 'bob')
print('friends = ', friends)
mehmonlar = []
mehmonlar.append(friends.pop(1))
mehmonlar.append(friends.pop(3))
mehmonlar.append(friends.pop(4))
print('mehmonlar = ', mehmonlar)