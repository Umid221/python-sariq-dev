import json

with open('JSON/students.json') as f:
    students = json.load(f)

for stud in students['student']:
    print(f"{stud['name']} {stud['lastname']}, {stud['year']}-kurs, {stud['faculty']} fakulteti talabasi")
