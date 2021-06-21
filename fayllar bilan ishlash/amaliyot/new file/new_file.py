malumot = input("ma'lumot kiriting: ")


with open("fayllar bilan ishlash/amaliyot/new file/ma'lumotlar.txt", 'a') as file:
    file.write(f"{malumot}\n")