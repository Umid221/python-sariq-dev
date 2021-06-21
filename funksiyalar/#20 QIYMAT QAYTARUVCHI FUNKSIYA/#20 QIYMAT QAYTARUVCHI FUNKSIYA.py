def malumotlar(ism, familiya, tug_yil, email, tug_joy='', tel_raqam=None):
    """Mijoz haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
    mijoz = {'ism':ism,
            'familiya':familiya,
            'tug_yil':tug_yil,
            'yosh':2021-tug_yil,
            'email':email,
            'tug_joy':tug_joy,
            'tel_raqam':tel_raqam}
    return mijoz
    
mijozlar = []
while True:
    ism = input('ismingizni kiriting: ')
    familiya = input('familiyangizni kiriting: ')
    tug_yil = int(input("Tug'ilgan yilingizni kiriting: "))
    email = input("emailingizni kiriting: ")
    tug_joy = input("Tug'ilgan joyingizni kiriting: ")
    tel_raqam = input("Telefon raqamingizni kiriting: ")
    m = malumotlar(ism, familiya, tug_yil, email, tug_joy, tel_raqam)
    mijozlar.append(m)
    keyingisi = input("keyingisini kiritasizmi(ha/yo'q)? ")
    if keyingisi != 'ha':
        break
for mijoz in mijozlar:
    print(mijoz)