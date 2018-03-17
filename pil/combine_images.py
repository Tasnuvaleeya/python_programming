from PIL import Image

arisha = Image.open("c.jpg")
we = Image.open("i.jpg")
area = (we.size)

print(arisha.size)
print(we.size)

arisha.paste(we,area)
arisha.show()