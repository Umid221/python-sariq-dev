print("dasturni to'xtatish uchun 'exit' yoki 'quit' deb yozing")
p = 'chipta narxi'
yosh = ''
while yosh != 'exit' or yosh != 'quit':
    yosh = input('yoshingizni kiriting: ')
    if yosh == 'exit' or yosh == 'quit':
        break
    elif int(yosh) <7:
        print(p, '2000 so\'m')
    elif int(yosh)<18:
        print(p, '3000 so\'m')
    elif int(yosh)<65:
        print(p, '10000 so\'m')
    else:
        print(p, 'bepul!')