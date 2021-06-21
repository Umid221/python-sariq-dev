class Shaxs:
    """Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
    
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info
        
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil

class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self,ism,familiya,passport,tyil,idraqam,manzil):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil
        self.fanlar = []
    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam
    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich
    
    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
        return info

    def fanga_yozil(self, fan):
        return self.fanlar.append(fan)
    
    def remove_fan(self, fan):
        if fan in self.fanlar:
            self.fanlar.remove(fan)
            return self.fanlar
        else:
            return "Siz bu fanga yozilmagansiz"

class Manzil:
    """Manzil saqlash uchun klass"""
    def __init__(self,uy,kocha,tuman,viloyat):
        """Manzil xususiyatlari"""
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat
    
    def get_manzil(self):
        """Manzilni ko'rish"""
        manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
        manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
        return manzil

class Fan:
    def __init__(self, nomi):
        self.nomi = nomi
    def get_info(self):
        return self.nomi

class Mijoz(Shaxs):
    def __init__(self, ism, familiya, passport, tyil, raqam):
        super().__init__(ism, familiya, passport, tyil)
        self.raqam = raqam
        self.discount = 2
    def get_info(self):
        info = f"{self.ism} {self.familiya}. "
        info += f"Raqami {self.raqam}. Chgirma miqdori {self.discount}%"
        return info
    
class Doimiy_mijoz(Mijoz):
    def __init__(self, ism, familiya, passport, tyil, raqam, maxsus_kod):
        super().__init__(ism, familiya, passport, tyil, raqam)
        self.maxsus_kod = maxsus_kod
        self_discount = 5
    def get_info(self):
        info = f"{self.ism} {self.familiya}. "
        info += f"Raqami {self.raqam}. Chgirma miqdori {self.discount}%"
        info += f"Mijozga berilgan maxsus kod {self.maxsus_kod}."
        return info
    def smth(self):
        return print('smth')

matem = Fan('matematika')
fizika = Fan("fizika")
bio = Fan("biologiya")
talaba_manzil = Manzil(12,'Olmazor',"Bog'bon","Samarqand")
talaba = Talaba("Valijon","Aliyev","FA112299",2000,"0000012",talaba_manzil)
talaba.fanga_yozil(matem)
talaba.fanga_yozil(bio)
talaba.fanga_yozil(fizika)
print(talaba.fanlar)
talaba.remove_fan(bio)
print(talaba.fanlar)