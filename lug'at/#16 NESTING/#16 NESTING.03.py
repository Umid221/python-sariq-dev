davlatlar = {
    "o'zbekiston":{'poytaxt':"toshkent",
                   'maydon':448978,
                   'aholi':33_000_000,
                   'pul birligi':"so'm"
                   },
    "rossiya":{'poytaxt':"moskva",
                   'maydon':17_098_246,
                   'aholi':144_000_000,
                   'pul birligi':"rubl"
                   },
    "aqsh":{'poytaxt':"vashington",
                   'maydon':9_631_418,
                   'aholi':327_000_000,
                   'pul birligi':"dollar"},
    "malayziya":{'poytaxt':"kuala-lumpur",
                   'maydon':329750,
                   'aholi':25_000_000,
                   'pul birligi':"rinngit"},
    "germaniya":{'poytaxt':'berlin',
                    'maydon':357_022,
                    'aholi':83_166_711,
                    'pul birligi':'yevro'}
    }
for davlat, info in davlatlar.items():
    print(f"\n{davlat.title()}ning poytaxti {info['poytaxt'].title()}"
            f"\nHududi: {info['maydon']} km kv."
            f"\nAholisi: {info['aholi']}"
            f"\nPul birligi: {info['pul birligi']}")

print('------------------------------------------------------')
mamlakat = input('Davlat nomini kiriting: ').lower()
check = davlatlar.get(mamlakat)
if check == None:
    print('Bizda bu davlat haqida ma\'lumot mavjud emas')
else:
    print(f"\n{mamlakat.title()}ning poytaxti {check['poytaxt'].title()}"
            f"\nHududi: {check['maydon']} km kv."
            f"\nAholisi: {check['aholi']}"
            f"\nPul birligi: {check['pul birligi']}")