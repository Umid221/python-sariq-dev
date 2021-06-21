import json

with open('JSON/api-result.json') as f:
    data = json.load(f)

print(data['query']['pages']['13801']['title'], '\n')
print(data['query']['pages']['13801']['extract'])