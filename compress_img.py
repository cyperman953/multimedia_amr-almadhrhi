from PIL import Image

img = Image.open(str(input('enter path Image open:')))
newImage = img.resize((1024, 768), Image.ANTIALIAS)         

newImage.save(input('enter path newImage save compress:'), optimize=True, quality=95)
if img==Image:
    print("save img")

newImage.show()
img.show()
