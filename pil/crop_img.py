from PIL import Image

img = Image.open("a.jpg")
area = (100, 100, 500, 500)
cropped_image = img.crop(area)
cropped_image.show()
img.show()
