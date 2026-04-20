#1
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating

    def describe_restaurant(self):
        print(f"Ресторан: {self.restaurant_name}, Кухня: {self.cuisine_type}, Рейтинг: {self.rating}")

    def open_restaurant(self):
        print(f"Ресторан {self.restaurant_name} открыт!")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, rating=0):
        super().__init__(restaurant_name, "Кафе-мороженое", rating)
        self.flavors = ["Ванильное", "Шоколадное", "Клубничное"]

    def show_flavors(self):
        print("Сорта мороженого:")
        for flavor in self.flavors:
            print(f"  - {flavor}")


ice_shop = IceCreamStand("Мороженка", 5)
ice_shop.show_flavors()

#2
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating

    def describe_restaurant(self):
        print(f"Ресторан: {self.restaurant_name}, Кухня: {self.cuisine_type}, Рейтинг: {self.rating}")

    def open_restaurant(self):
        print(f"Ресторан {self.restaurant_name} открыт!")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, location="Не указана", work_time="10:00-22:00", rating=0):
        super().__init__(restaurant_name, "Кафе-мороженое", rating)
        self.flavors = ["Ванильное", "Шоколадное", "Клубничное"]
        self.location = location
        self.work_time = work_time

        # Разные типы мороженого
        self.stick_icecream = []  # мороженое на палочке
        self.soft_icecream = []  # мягкое мороженое
        self.scoop_icecream = []  # шариковое мороженое

    # Вывод списка сортов
    def show_flavors(self):
        print("Сорта мороженого:")
        for flavor in self.flavors:
            print(f"  - {flavor}")

    #  а) Локация и время работы
    def show_info(self):
        print(f"Кафе: {self.restaurant_name}")
        print(f"Локация: {self.location}")
        print(f"Время работы: {self.work_time}")

    # б) Добавление и удаление сортов
    def add_flavor(self, flavor):
        self.flavors.append(flavor)
        print(f"Сорт '{flavor}' добавлен!")

    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)
            print(f"Сорт '{flavor}' удалён!")
        else:
            print(f"Сорта '{flavor}' нет в списке!")

    # в) Проверка наличия сорта
    def has_flavor(self, flavor):
        if flavor in self.flavors:
            print(f"Да, {flavor} есть в наличии!")
            return True
        else:
            print(f"Нет, {flavor} отсутствует!")
            return False

    # г) Методы для разных типов
    # Мороженое на палочке
    def add_stick_icecream(self, name):
        self.stick_icecream.append(name)
        print(f"Мороженое на палочке '{name}' добавлено в меню!")

    def show_stick_icecream(self):
        print("Мороженое на палочке:")
        for item in self.stick_icecream:
            print(f"  - {item}")

    # Мягкое мороженое
    def add_soft_icecream(self, name):
        self.soft_icecream.append(name)
        print(f"Мягкое мороженое '{name}' добавлено в меню!")

    def show_soft_icecream(self):
        print("Мягкое мороженое:")
        for item in self.soft_icecream:
            print(f"  - {item}")

    # Шариковое мороженое
    def add_scoop_icecream(self, name):
        self.scoop_icecream.append(name)
        print(f"Шариковое мороженое '{name}' добавлено в меню!")

    def show_scoop_icecream(self):
        print("Шариковое мороженое:")
        for item in self.scoop_icecream:
            print(f"  - {item}")


#ПРИМЕР ИСПОЛЬЗОВАНИЯ

# Создаём кафе-мороженое
my_cafe = IceCreamStand("Сладкий Рожок", "ул. Центральная, 15", "09:00-23:00", 5)

# а) Показываем локацию и время
my_cafe.show_info()
print()

# Показываем основные сорта
my_cafe.show_flavors()
print()

# б) Добавляем и удаляем сорта
my_cafe.add_flavor("Мятное")
my_cafe.add_flavor("Карамельное")
my_cafe.remove_flavor("Клубничное")
print()

# в) Проверяем наличие
my_cafe.has_flavor("Ванильное")
my_cafe.has_flavor("Фисташковое")
print()

# г) Работа с разными типами мороженого
my_cafe.add_stick_icecream("Фруктовый лёд")
my_cafe.add_stick_icecream("Эскимо")
my_cafe.show_stick_icecream()
print()

my_cafe.add_soft_icecream("Ванильный рожок")
my_cafe.add_soft_icecream("Клубничный твист")
my_cafe.show_soft_icecream()
print()

my_cafe.add_scoop_icecream("Три шарика с шоколадом")
my_cafe.add_scoop_icecream("Фисташка с орехами")
my_cafe.show_scoop_icecream()