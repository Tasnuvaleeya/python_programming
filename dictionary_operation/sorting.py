from operator import itemgetter

users = [
    {'fname': 'Tasnuva', 'lname':'Zaman'},
    {'fname': 'Sadia', 'lname':'Lamia'},
    {'fname': 'Sabita', 'lname':'Zinia'},
    {'fname': 'Ahsanuz', 'lname':'Zenith'},
    {'fname': 'Tasnuva', 'lname':'Leeya'},
    {'fname': 'Tasnuva', 'lname':'Riya'},
    {'fname': 'Shahriar', 'lname':'Siddik'},
]

# for x in sorted(users, key=itemgetter('fname')):
#     print(x)
print("---------------------------------------------")

for x in sorted(users, key=itemgetter('fname', 'lname')):
    print(x)