from operator import attrgetter

class User:
    def __init__(self, x, y):
        self.name = x
        self.user_id= y
    def __repr__(self):
        return self.name + " : " + str(self.user_id)

users =[
    User('Leeya', 1),
    User('Lamia', 22),
    User('Zinia', 66),
    User('Zenith', 33)

]
for user in users:
    print(user)
    print('----------------')

for user in sorted(users, key=attrgetter('name')):
    print(user)