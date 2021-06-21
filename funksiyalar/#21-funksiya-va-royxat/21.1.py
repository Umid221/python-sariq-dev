def bosh_harf_qil(sozlar):
    yangi_sozlar = sozlar[:]
    for i in range(len(sozlar)):
        yangi_sozlar[i] = sozlar[i].title()
    return yangi_sozlar
l = ['ali', 'vali', "gani"]
print(bosh_harf_qil(l))
print(l)

def bahola(talabalar):
    lugat = {}
    for i in range(len(talabalar)):
        talaba = talabalar[i]
        baho = input(f"{talaba}ning bahosini kiriting: ")
        lugat[talaba] = baho
    return lugat

print(bahola(l))
print(l)