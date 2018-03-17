class Mario():
    def move(self):
        print('I am Moving')
class Shroom():
    def eat_shromm(self):
        print('Now I am big')

class BigMario(Mario, Shroom):
    pass
bm = BigMario()

bm.move()
bm.eat_shromm()