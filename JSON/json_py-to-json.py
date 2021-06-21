import json

data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}
data_json = json.dumps(data)
print(data_json)

with open('JSON\py-to-json.json', 'w') as f:
    json.dump(data, f)