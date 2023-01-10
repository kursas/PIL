#Parašykite programą, kuriai padavus nuotrauką, ir nurodžius pikselio R G B reikšmes,
# visi pikseliai, kurių nors viena reikšmė viršija jūsų nurodytą ribą,
# būtų pakeisti juodais, o likusieji baltais.
from PIL import Image


def turn_binary(img, r, g, b):
    img = Image.open(img)
    data = img.getdata()
    new_data = []
    black = 0, 0, 0
    white = 255, 255, 255
    for pixel in data:
        if pixel[0] >= r or pixel[1] >= g or pixel[2] >= b:
            new_data.append(black)
        else:
            new_data.append(white)

    img.putdata(new_data)
    return img


image = turn_binary('D:/DUMENYS/DARIUS/Desktop/dog.jpg', 255, 255, 150)
image.show()
image.save("D:/DUMENYS/DARIUS/Desktop/black_white_dog.jpg")

#output
Process finished with exit code 0
