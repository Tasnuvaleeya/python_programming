from PIL import Image
img = Image.open("a.jpg")
print(img.size)
print(img.format)
img.show()
