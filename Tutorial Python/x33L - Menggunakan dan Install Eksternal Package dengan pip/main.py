from PIL import Image
import numpy as np

a = np.array([1, 2, 3, 4])

b = np.array([1, 2, 3, 4])

print(a+b)

im = Image.open("wallpaper.jpg")

im.show()
print("Format        : " + str(im.format))
print("Ukuran file   : " + str(im.size))
print("Mode          : " + str(im.mode))
