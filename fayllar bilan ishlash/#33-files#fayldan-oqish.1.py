with open('D:/programming/python/python.sariq.dev/fayllar bilan ishlash/pi.txt') as fayl:
    pi = fayl.read()
pi = pi.rstrip()
pi = pi.replace('\n','')
pi = float(pi)
print(pi)
print(type(fayl))

with open('ustozlar.txt', 'w') as file:
    file.write("anvar narzullaev\n")

with open('ustozlar.txt', 'a') as faayl:
    faayl.write("alijon Valiyev")