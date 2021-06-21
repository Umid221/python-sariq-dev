def yil_top(ism, yosh):
    """Foydalanuvchi yoshiga ko'ra uning tug'ilan yilini hisoblaydigan funksiya"""
    print(f"{ism.title()}, siz {2021-yosh}-yilda tug'ilgansiz")
yil_top('umid', 21)
print('--------------------------------------')
def kv_kub_hisobla(son):
    """"Foydalanuvchi kiritgan sonning kvadrati va kubini hisoblaydigan funksiya"""
    print(f"{son}**2={son**2}")
    print(f"{son}**3={son**3}")
kv_kub_hisobla(4)
print('--------------------------------------')
def juft_toq(raqam):
    """Foydalanuvchi kiritgan sonning juft yoki toqligini aniqlovchi funksiya"""
    if raqam%2==0:
        print("Kiritgan raqamingiz juft")
    else:
        print("Kiritgan raqamingiz toq")
juft_toq(88)
print('--------------------------------------')
def maximum(a,b):
    """Foydalanuvchi kiritgan sonlarning kattasini topuvchi funksiya"""
    if a<b: print(b)
    elif a>b: print(a)
    else: print("Sonlar teng")
maximum(23,34)
print('--------------------------------------')
def daraja_top(x,y=2):
    """Birinchi kiritilgan sonning ikkinchi kiritilgan songa ko'tarilgan 
    darajasi. Agar ikkinchi son kiritilmasa kvadratni hisoblaydi"""
    print(f"{x}**{y}={x**y}")
daraja_top(3,6)
daraja_top(4)
print('--------------------------------------')
def qoldiqsiz_bolinadi(z):
    """Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan
     sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya"""
    for i in range(2, 11):
        if z % i == 0:
            print(f"{z} {i} ga qoldiqsiz bo'linadi")
qoldiqsiz_bolinadi(8237864)