from PIL import Image

baby = Image.open("a.jpg")
square_img = baby.resize((250, 250))
flip_baby = baby.transpose(Image.FLIP_LEFT_RIGHT)
flip_baby1 = baby.transpose(Image.FLIP_TOP_BOTTOM)
spin_baby= baby.transpose(Image.ROTATE_90)

# baby.show()
spin_baby.show()
# square_img.show()
# flip_baby1.show()
# print(baby.size)