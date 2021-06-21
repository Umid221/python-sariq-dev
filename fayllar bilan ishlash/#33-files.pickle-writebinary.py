import pickle

talaba1 = {'ism':'hasan', 'familiya':'husanov', 'tyil':2003, 'kurs': 2}
talaba2 = {'ism':'alijon', 'familiya':'valiyev', 'tyil':2004, 'kurs': 1}

with open('info', 'wb') as fayl:
    pickle.dump(talaba1, fayl)
    pickle.dump(talaba2, fayl)