import json

data = {
    "products": [
        {"name": "Шоколад", "price": 50, "available": True, "weight": 100},
        {"name": "Кофе", "price": 100, "available": False, "weight": 250},
        {"name": "Чай", "price": 70, "available": True, "weight": 50}
    ]
}

with open('products.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)


with open('products.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for product in data['products']:
    print(f"Название: {product['name']}")
    print(f"Цена: {product['price']}")
    print(f"Вес: {product['weight']}")
    print("В наличии" if product['available'] else "Нет в наличии!")
    print()

#2
with open('products.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print("Добавление нового продукта:")
name = input("Название: ")
price = int(input("Цена: "))
weight = int(input("Вес: "))
available = input("В наличии? (да/нет): ").lower() == 'да'

new_product = {
    "name": name,
    "price": price,
    "available": available,
    "weight": weight
}

data['products'].append(new_product)


with open('products.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)


print("\nИтоговый список продуктов:")
for product in data['products']:
    print(f"Название: {product['name']}")
    print(f"Цена: {product['price']}")
    print(f"Вес: {product['weight']}")
    print("В наличии" if product['available'] else "Нет в наличии!")
    print()
#3
ru_en = {}

with open('en-ru.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        parts = line.split(' - ')
        eng = parts[0].strip()
        rus_words = parts[1].strip().split(', ')

        for rus in rus_words:
            rus = rus.strip()
            if rus in ru_en:
                ru_en[rus].append(eng)
            else:
                ru_en[rus] = [eng]

sorted_items = sorted(ru_en.items())

with open('ru-en.txt', 'w', encoding='utf-8') as f:
    for rus, eng_list in sorted_items:
        eng_str = ', '.join(sorted(eng_list))
        f.write(f"{rus} – {eng_str}\n")

print("Русско-английский словарь создан в файле ru-en.txt")