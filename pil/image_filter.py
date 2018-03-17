from PIL import Image
from PIL import ImageFilter

baby = Image.open("a.jpg")
black_white = baby.convert("L")
blur_image = baby.filter(ImageFilter.BLUR)
detail = baby.filter(ImageFilter.DETAIL)
edges = baby.filter(ImageFilter.FIND_EDGES)

blur_image.show()
detail.show()
edges.show()
# black_white.show()