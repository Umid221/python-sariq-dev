from uuid import uuid4

class Shaxs:
    __number = 0
    """Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        self.__id = uuid4()
        self.__number += 1

    def get_id(self):
        return self.__id
    
    @classmethod
    def get_number(cls):
        return cls.__number

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
    __talabalar_soni = 0
    def __init__(self,ism,familiya,passport,tyil,manzil):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.bosqich = 1
        self.manzil = manzil
        self.fanlar = []
        self.__idraqam = uuid4()
        self.__talabalar_soni += 1

    @classmethod
    def get_talaba_soni(cls):
        return cls.__talabalar_soni

    def get_id(self):
        """Talabaning ID raqami"""
        return self.__idraqam
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
