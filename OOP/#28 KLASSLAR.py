class User:
    def __init__(self, name, nickname, email, birthyear):
        self.name = name
        self.nickname = nickname
        self.email = email
        self.birthyear = birthyear
    def get_info(self):
        return f'foydalanuvchi: {self.nickname}\n ismi: {self.name}\n e-pochta manzili:{self.email}'
    def get_age(self, current_year):
        return current_year-self.birthyear

user1 = User('Umid', 'umid22', 'umid@gmail.com', 2000)
user2 = User('John', 'Mr John', 'JJJJJJJ@gmail.com', 2001)
print(user1.name)
print(user1.get_age(2021))
