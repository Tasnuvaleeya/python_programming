from PIL import Image

arisha = Image.open("a.jpg")
we = Image.open("c.jpg")
print(we.size)
print(arisha.size)
# print(arisha.mode)
r, g, b = arisha.split()
r1, g1, b1 = we.split()
new_img = Image.merge("RGB", (r1, g, b1))
# new_img = Image.merge('RGB', (b, g, r))

new_img.show()
