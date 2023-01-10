# Turime logo su peršviečiamu fonu, dydis 128*128.
# Atsisiųskite, ir perdarykite taip, kad nuo viršaus ir
# apačios nusiimtų po 28 eilutes pikselių. Išsisaugokite,
# nes naudosime sekančioms užduotims.
# from PIL import Image
# im = Image.open("D:/DUMENYS/DARIUS/Desktop/logo.png")
# frame = (0, 28, 128, 100)
# region = im.crop(frame)
# region.save('D:/DUMENYS/DARIUS/Desktop/logo_cropped.png')

#linos variantas
# Turime logo su peršviečiamu fonu, dydis 128*128. Atsisiųskite, ir perdarykite taip, kad nuo viršaus ir apačios
# nusiimtų po 28 eilutes pikselių. Išsisaugokite, nes naudosime sekančioms užduotims.
from PIL import Image
img = Image.open("D:/DUMENYS/DARIUS/Desktop/logo.png")
# x-min, y-min, x-max, y-max
crop_box = (0,28,128,100)
cropped_immage = img.crop(crop_box)
cropped_immage.show()
img.save("D:/DUMENYS/DARIUS/Desktop/croped_logo.png")

#output
Process finished with exit code 0
