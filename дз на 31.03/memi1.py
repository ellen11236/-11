from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os


# ЗАДАНИЕ 1
img = Image.open("обмем.jpg")
img.show()

w, h = img.size
print("Размер:", w, "x", h)
print("Формат:", img.format)
print("Цветовая модель:", img.mode)

# ЗАДАНИЕ 2
small = img.resize((w // 5, h // 3))
small.save("обмем_small.jpg")

mirror_h = img.transpose(Image.FLIP_LEFT_RIGHT)
mirror_h.save("обмем_mirror_h.jpg")

mirror_v = img.transpose(Image.FLIP_TOP_BOTTOM)
mirror_v.save("обмем_mirror_v.jpg")

# ЗАДАНИЕ 3
files = ["обмем.jpg", "уйдумем.jpg", "кодмэм.jpg", "егэмем.jpg"]
os.makedirs("../filtered", exist_ok=True)

for f in files:
    img = Image.open(f)
    filtered = img.filter(ImageFilter.CONTOUR)
    filtered.save("filtered/" + f)

# ЗАДАНИЕ 4
image = Image.open('уйдумем.jpg')

watermark_text = 'FVVVVVVPDFNNNNNNNNNJJJJJO'
text_position = (100, 100)
font = ImageFont.load_default()
draw = ImageDraw.Draw(image)
draw.text(text_position, watermark_text, font=font, fill=(250, 250, 250))

image.save('лалала.jpg')