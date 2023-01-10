#sukurkite funkciją, kuri priimtų paveikslėlį
#kontrasto, spalvingumo, aštrumo ir ryškumo reikšmes išsaugoti ar ne reikšmę
#ir atitinkamai pakoreguotų paveikslėlio nustatymus.
# Parodytų nuotrauką ekrane. Priklausomai nuo pasirinkimo, išsaugotų arba ne.
# Išsaugokite faile, prie originalaus pavadinimo pridėję pvz. '_modified', tarkime dog_modified.jpg.
from PIL import Image, ImageEnhance
import os
def enhance_image(pic, contrast, color, sharpness, brightness, save=False):
    img = Image.open(pic)
    enhc = ImageEnhance.Contrast(img)
    img = enhc.enhance(contrast)
    enhc = ImageEnhance.Color(img)
    img = enhc.enhance(color)
    enhc = ImageEnhance.Brightness(img)
    img = enhc.enhance(brightness)
    enhc = ImageEnhance.Sharpness(img)
    img = enhc.enhance(sharpness)
    if save:
        location = os.path.splitext(pic)[0]
        ext = os.path.splitext(pic)[1]
        img.save(f'{location}_modified{ext}')
    img.show()

enhance_image('D:/DUMENYS/DARIUS/Desktop/dog.jpg', 2, 0, 4, 1, True)

#output
Process finished with exit code 0
