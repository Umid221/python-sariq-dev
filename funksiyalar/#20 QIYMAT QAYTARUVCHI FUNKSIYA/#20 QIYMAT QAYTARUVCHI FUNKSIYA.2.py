def kattasini_top(a,b,c):
    """Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya"""
    if a >b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

def aylana(r):
    """Foydalanuvchidan aylaning radiusini qabul qilib olib, 
    uning radiusini, diametrini, perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya"""
    info = {'radius':r,
            'diametr':r*2,
            'perimetr':2*3.14*r,
            'yuzi':3.14*(r**2)}
    return info

def tub_sonmi(a):
    for i in range(2,a):
        if a%i == 0:
            return
    return a

def tub_sonlar(m, n):
    """Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya.Birinchi kichik sonni kiriting!!!"""
    tubsonlar = []
    for item in range(m, n+1):
        son = tub_sonmi(item)
        if son != None:
            tubsonlar.append(son)            
    return tubsonlar

def fibanocci(q):
    sonlar = []
    while len(sonlar)<q:
        uzunlik = len(sonlar)
        if uzunlik==0 or uzunlik==1:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[uzunlik-2]+sonlar[uzunlik-1])
    return sonlar
print(fibanocci(2))