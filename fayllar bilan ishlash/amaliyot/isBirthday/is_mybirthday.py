filename = 'D:/programming/python/python.sariq.dev/fayllar bilan ishlash/amaliyot/pi_million_digits.txt'
with open(filename) as file:
    son = file.read()
    
def is_mybirthday(kun):
    if str(kun) in son:
        return True
    else:
        return False

print(is_mybirthday(230664))