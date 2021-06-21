davlatlar = ["O'zbekiston", "Turkiya", "AQSh", "Rossiya", "Xitoy", "Malayziya", "Misr"]
print('davlatlar', davlatlar)

print("ro'yxat uzunligi: ", len(davlatlar))
print('sorted ro\'yxat: ', sorted(davlatlar))
print('teskari tartiblangan ro\'yxat: ', sorted(davlatlar, reverse=True))
print('asl ro\'yxat: ', davlatlar)

davlatlar.reverse()
print('reversed: ', davlatlar)

davlatlar.sort()
print('sort metodi: ', davlatlar)

davlatlar.sort(reverse=True)
print('teskari sort metodi: ', davlatlar)

juft = list(range(120, 1200, 2))
print(sum(juft))
print(max(juft)-min(juft))
print('elementlar soni ',len(juft))
print(juft[:20])
print(juft[260:280])
print(juft[520:])

taomlar = ['osh', 'sho\'rva', 'kabob', 'do\'lma', 'norin']
nonushta = taomlar[:]
nonushta.pop(3)
nonushta.remove('kabob')
nonushta.append('sut')
nonushta.insert(2, 'bo\'tqa')
print('taomlar: ',taomlar)
print('nonushta: ', nonushta)
nonushta = tuple(nonushta)
nonushta[0] = 'qaymoq va non'