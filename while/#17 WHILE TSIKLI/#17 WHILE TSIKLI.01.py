kirish = 'yaxshi ko\'rgan kitoblaringizni kiriting'
kirish += '(dastur to\'xtashi uchun "stop" deb yozing):'
kitob = ''
while kitob != 'stop':
    kitob = input(kirish)
    if kitob == 'stop':
        break
print('rahmat')