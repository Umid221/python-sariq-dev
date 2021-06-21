import json

talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""
talaba = json.loads(talaba_json)
print(talaba['ism'])
print(talaba['familiya'])

with open('JSON\json-to-py.json', 'w') as f:
    json.dump(talaba_json, f)