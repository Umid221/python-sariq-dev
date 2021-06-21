import random as r
print("Keling, o'ylagan sonni topish o'ynaymiz!")
def son_topaman():
    x = int(input('biror son kiriting: '))
    son1 = r.choice(range(1,x+1))
    print(f"1 dan {x} gacha son o'yladim. Topa  olasizmi?")
    son2 = 0
    n = 0
    while son2!=son1:
        son2 = int(input('>>>'))
        n += 1
        if son2>son1:
            print("Xato, men o'ylagan son bundan kichikroq. Yana harakat qiling:")
        elif son1>son2:
            print("Xato, men o'ylagan son bundan kattaroq. Yana harakat qiling:")
    print(f"TOPDINGIZ! {son1} sonini o'ylagan edim. {n} ta taxmin bilan topdingiz. Tabriklayman!")
    return n
def son_top():
    p = int(input('oraliqning birinchi sonini kiriting: '))
    q = int(input('oxirgi sonini kiriting: '))
    print(f"\n{p} dan {q} gacha son o'ylang, men topishga harakat qilaman")
    input("Son o'ylagan bo'lsangiz enter tugmasini bosing.")
    javob = ''
    m = 1
    while javob != 't':
        num = r.randint(p,q)
        javob = input(f"Siz {num} sonini o'yladingiz: to'g'ri(T), men o'ylagan son bundan kattaroq(+), yoki kichikroq(-)? ").lower()
        if javob == '+':
            p = num+1
            m += 1
        elif javob == '-':
            q = num-1
            m += 1
        else:
            print('"t", "-" yoki "+" belgilaridan boshqa belgi qabul qilinmaydi!')
    print(f"Soningizni {m} ta taxmin bilan topdim")
    return m
javob = 1
while javob == 1:
    n = son_topaman()
    m = son_top()
    if m<n:
        print('men yutdim!')
    elif m>n:
        print('siz yutdingiz!')
    else:
        print('durrang!')
    javob = int(input('yana o\'ynashni xohlaysizmi(ha=1/yo\'q=0)? '))
