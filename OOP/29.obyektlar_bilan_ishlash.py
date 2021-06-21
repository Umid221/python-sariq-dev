class Avto:
    def __init__(self, model, rang, korobka, narx):
        self.model = model
        self.rang = rang
        self.korobka = korobka
        self.narx = narx
        self.kilometr = 0
    def get_info(self):
        return f"{self.rang} rangli {self.model} modeliga tegishli {self.kilometr} km yurgan {self.korobka} mashinaning narxi {self.narx}."
    def update_km(self, kilometr):
        self.kilometr = kilometr

class Avtosalon:
    def __init__(self, nomi, manzili):
        self.nomi = nomi
        self.manzili = manzili
        self.sotuvdagi_avtolar = []
    def set_avtolar(self, yangi_avto):
        return self.sotuvdagi_avtolar.append(yangi_avto)
    def get_info(self):
        return [avto.get_info() for avto in self.sotuvdagi_avtolar]

avto1 = Avto('malibu', 'oq', 'avtomat', 20000)
avto2 = Avto('BMW X9', 'qora', 'avtomat', 40000)
avtosalon1 = Avtosalon('5-avtosalon', 'Buxoro, Mustaqillik 16')
avtosalon1.set_avtolar(avto1)
avtosalon1.set_avtolar(avto2)
print(avtosalon1.get_info())

# print(dir(Avtosalon))
print(avto1.__dict__)
print(avtosalon1.__dict__)