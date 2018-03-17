class Parent():

    def last_name(self):
        print('Zaman')

class Child(Parent):

    def first_name(self):
        print('Tasnuva')

    def last_name(self):                 # Overriding
        print("Leeya")

r = Child()
r.last_name()
r.first_name()
