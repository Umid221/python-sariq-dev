def talabalar(ism, familiya, **malumotlar):
    malumotlar['ism'] = ism
    malumotlar['familiya'] = familiya
    return malumotlar
print(talabalar('ali', 'valiyev', tyil=2000))