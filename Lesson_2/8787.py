
a = {
    "first_name": 'Nurik',
    "last_name": "Shadmanov",
    "middle names": "Kengebekovich",
    "telephone": "0709 08 08 20",
    "adres": "Dgal29 11B"}

del a["telephone"]

print(a["last_name"])

#Часть2

a = {
    "first_name": 'Nurik',
    "last_name": "Shadmanov",
    "middle names": "Kengebekovich",
    "telephone": "0709 08 08 20",
    "adress": "Dgal29 11B"}


for i in a.values():

    print(i)
for k, v in a.items():
    print(k,v)
a.clear()
print(a)
