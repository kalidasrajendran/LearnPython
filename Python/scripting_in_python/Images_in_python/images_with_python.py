print('-------*images with python*-------')
# pillow package
from PIL import Image, ImageFilter

img = Image.open(".\pics\pikachu.jpg")

print('-------*pic information*-------')
print(img.format)
print(img.size)
print(img.mode)
# print(dir(img))

print('-------*pic contour*-------')
filtered_img = img.filter(ImageFilter.CONTOUR)
filtered_img.save("contour.png", 'png')

print('-------*pic blur*-------')
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save("blur.png", 'png')

print('-------*pic gray scale*-------')
filtered_img = img.convert('L')
filtered_img.save("gray.png", 'png')

print('-------*pic rotate*-------')
filtered_img = img.rotate(-180)
filtered_img.save("rotate.png", 'png')
#filtered_img.show()

print('-------*pic resize*-------')
filtered_img = img.resize((300, 300))
filtered_img.save("resize_300x300.png", 'png')
# filtered_img.show()

print('-------*pic resize with aspect_ratio*-------')
filtered_img = img
filtered_img.thumbnail((300, 100))
filtered_img.save("resize_aspect_300x100.png", 'png')

print('-------*pic crop*-------')
box = (100, 100, 400, 400)
filtered_img = img.crop(box)
filtered_img.save("cropped.png", 'png')