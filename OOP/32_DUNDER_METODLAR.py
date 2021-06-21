class Talaba:
    def __init__(self, ism, familiya, tyil, passport, bosqich):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.passport = passport
        self.bosqich = bosqich

    def __repr__(self):
        return f"Talaba: {self.ism.title()} {self.familiya.title()}"
    
    def __lt__(self, boshqa_talaba):
        return self.bosqich < boshqa_talaba.bosqich
    
    def __eq__(self, boshqa_talaba):
        return self.bosqich == boshqa_talaba.bosqich

    def __le__(self, boshqa_talaba):
        return self.bosqich <= boshqa_talaba.bosqich
    
class Fan:
    def __init__(self, nomi):
        self.nomi = nomi
        self.talabalar = []

    def __repr__(self):
        return f"{self.nomi.title()} fani"

    def add_student(self, *students):
        for student in students:
            if isinstance(student, Talaba):
                self.talabalar.append(student)
            else:
                print("Talaba obyektini kiriting")

    def __len__(self):
        return len(self.talabalar)

    def __getitem__(self, index):
        return self.talabalar[index]

    def __setitem__(self, index, val):
        if isinstance(val, Talaba):
            self.talabalar[index]=val
    
    def __add__(self, y):
        if isinstance(y, Fan):
            yangi_fan = Fan(f"{self.nomi} {y.nomi}")
            yangi_fan.talabalar = self.talabalar + y.talabalar
            return yangi_fan
        elif isinstance(y, Talaba):
            self.add_student(y)
        else:
            print(f"Fanga {type(y)} qo'shib bo'lmaydi")

    def __call__(self, *param):
        if param:
            for talaba in param:
                self.add_student(talaba)
        else:
            return [talaba for talaba in self.talabalar]

    def __sub__(self, y):
        """talaba passportiga ko'ra talabani fan ro'yxatidan chiqarib tashlaydigan metod"""
        for talaba in self.talabalar:
            if talaba.passport == y:
        # if isinstance(y, Talaba) and y in self.talabalar:
                return self.talabalar.remove(talaba)
        return print("Siz noma'lum passport kiritdingiz")

talaba1 = Talaba("Umid", "najimov", 2000, 'SX1234567', 3)
talaba2 = Talaba('Ali', 'Valiyev', 2003, 'AJ0987654', 1)
talaba3 = Talaba('Hasan', 'husanov', 2001, 'AX3456788', 2)
talaba4 = Talaba('Soli', 'Choriyev', 2001, 'AS2345678', 2)
talaba5 = Talaba('Ali', "Aliyev", 1999, 'AS3456789', 3)
talaba6 = Talaba('Murod', 'Aliyrv', 1998, 'LS1234789', 4)
fan1 = Fan('matematika')
fan2 = Fan('kimyo')

print(talaba2, talaba1>talaba4, talaba4==talaba3, talaba2 >= talaba6)
print(fan1)
fan1.add_student(talaba1, talaba2, talaba3)
fan2.add_student(talaba4, talaba5, talaba6)
print(fan1.talabalar)
print(len(fan2))
print(fan1[2], fan2[1])
fan2[1]=talaba1
print(fan2[1])
print(fan1+fan2)
print(fan1())
fan2(talaba2)
print(fan1)
print(fan2)
print(fan1.talabalar)
print(fan2.talabalar)
fan2-'SX1234567'
print(fan2.talabalar)