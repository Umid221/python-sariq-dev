import telebot
from soz_top import soz_top

TOKEN = '1771652376:AAEx2gx6jrkxGs0oKyLCUv15yrdV9mehLTA'
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = "Assalomu alaykum. Xush kelibsiz!"
    javob += "\nO'yinni boshlash uchun botga 'play' so'zini yuboring"
    bot.reply_to(message, javob)

@bot.message_handler(command = ['play'])
def start_game(message):
    from uzwords import words
    from random import choice
    word = choice(words)
    # return word
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

bot.polling()