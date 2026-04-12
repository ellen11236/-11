from PIL import Image, ImageDraw, ImageFont

# ========== 7.1 Обрезка ==========
img = Image.open('postcard.jpg')
cropped_img = img.crop((0, 0, img.width, img.height - 100))
cropped_img.save('postcard_cropped.jpg')
print("Изображение обрезано и сохранено")

# ========== 7.2 Словарь ==========
holidays = {
    'Новый год': 'newy.jpg',
    '8 марта': 'march8.jpg',
    'День рождения': 'birth.jpg',
    '23 февраля': 'feb23.jpg'
}

holiday = input("К какому празднику? (Новый год, 8 марта, День рождения, 23 февраля): ")

if holiday in holidays:
    img = Image.open(holidays[holiday])
    img.show()
else:
    print("Такого праздника нет в списке")

# ========== 7.3 Добавление текста ==========
holiday = input("К какому празднику нужна открытка? ")
name = input("Введите имя: ")

if holiday in holidays:
    img = Image.open(holidays[holiday])
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except:
        font = ImageFont.load_default()

    text = f"{name}, поздравляю!"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    x = (img.width - text_width) // 2
    y = 50

    draw.text((x, y), text, fill=(255, 0, 0), font=font)
    img.save('greeting_card.png')
    img.show()
    print("Сохранено как greeting_card.png")
else:
    print("Такого праздника нет")