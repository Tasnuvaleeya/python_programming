from PIL import Image

arisha = Image.open("a.jpg")
# print(arisha.mode)
r, g, b = arisha.split()
r.show()
g.show()
b.show()