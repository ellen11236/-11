class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Ресторан: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Ресторан {self.restaurant_name} открыт!")


newRestaurant = Restaurant("Очаг", "Грузинская")

print(newRestaurant.restaurant_name)
print(newRestaurant.cuisine_type)


newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()


#2
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Ресторан: {self.restaurant_name}, Кухня: {self.cuisine_type}")


rest1 = Restaurant("Итальянский дворик", "Итальянская")
rest2 = Restaurant("Суши Wok", "Японская")
rest3 = Restaurant("Бургерная", "Американская")

rest1.describe_restaurant()
rest2.describe_restaurant()
rest3.describe_restaurant()

#3
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating  # начальный рейтинг

    def describe_restaurant(self):
        print(f"Ресторан: {self.restaurant_name}, Кухня: {self.cuisine_type}, Рейтинг: {self.rating}")

    def open_restaurant(self):
        print(f"Ресторан {self.restaurant_name} открыт!")

    def update_rating(self, new_rating):
        self.rating = new_rating
        print(f"Рейтинг ресторана {self.restaurant_name} обновлён до {self.rating}")


rest = Restaurant("Очаг", "Грузинская", 4)
rest.describe_restaurant()
rest.update_rating(5)
rest.describe_restaurant()