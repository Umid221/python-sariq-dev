def soz_top():
    def get_word():
        from uzwords import words
        from random import choice
        word = choice(words)
        return word
    word  = get_word()
    print(f"Мен {len(word)} хонали сўз ўйладим. Топа оласизми?")
    javob = ['-']*len(word)
    print(''.join(javob), '\n')
    harflar = ''
    while True:
        harf = input('Ҳарф киритинг: ')
        if harf in harflar:
            print("Сиз бу ҳарфни олдинроқ киритган эдингиз. Бошқа ҳарф киритинг")
            continue
        n = -1
        harflar += harf
        for char in word:
            n += 1
            if harf == char:
                print(f"{harf} ҳарфи тўғри")
                javob[n] = harf
        print(''.join(javob))
        
        if ''.join(javob) != word:
            print(f'Бу вақтгача киритган ҳарфларингиз: {harflar}')
        else:    
            print(f"Табриклайман! {word} сўзини {len(harflar)+1} та уринишда топдингиз.")
            break