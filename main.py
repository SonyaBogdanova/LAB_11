"LAB_11"

def p1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Название Ресторана: {self.restaurant_name}\nКухня:{self.cuisine_type} Восточноевропейская")

        def open_restaurant(self):
            print("Ресторан сейчас открыт -_-")

    newRestaurant = Restaurant("Three Broomsticks"," ")
    print(newRestaurant.restaurant_name)
    print(newRestaurant.cuisine_type)

    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()

def p2():

    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Название ресторана: {self.restaurant_name} \nКухня: {self.cuisine_type} \n")

        def open_restaurant(self):
            print("Ресторан сейчас открыт")


    for i in range (1,4):
        print('------------------------------------------')
        a = input('Введите имя ресторана: ')
        b = input('Какая кухня будет в этом ресторане? ')
        print('------------------------------------------')
        restauranti = Restaurant(a, b)
        restauranti.describe_restaurant()
        print('\n')
    print('-------------------------------------------------')
    print('-------------------------------------------------')

    #Ниже просто для красоты примеры написаны
    restaurant1 = Restaurant("ドラゴンアイ", "Японская")
    restaurant1.describe_restaurant()

    restaurant2 = Restaurant("Three Broomsticks", "Восточноевропейская")
    restaurant2.describe_restaurant()

    restaurant3 = Restaurant("Escargot Lumineux", "Французская")
    restaurant3.describe_restaurant()

def p3():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, initial_rating):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = initial_rating

        def describe_restaurant(self):
            print(f"Название ресторана {self.restaurant_name} \nКухня: {self.cuisine_type}Японская")

        def open_restaurant(self):
            print("Ресторан сейчас открыт")

        def update_rating(self, new_rating):
            self.rating = new_rating
            print(f"Рейтинг ресторана {self.restaurant_name} был обновлен до {self.rating}")

    restaurant1 = Restaurant("'ドラゴンアイ'", "Японская", 2)
    print(f"Изначальынй рейтинг ресторана {restaurant1.restaurant_name} = {restaurant1.rating}")
    restaurant1.update_rating(4.57)
    print(f"Новый рейтинг ресторана {restaurant1.restaurant_name} = {restaurant1.rating}")

    print('-------------------------------------------------')
    print('-------------------------------------------------')

    Restaurant2 = Restaurant("ドラゴンアイ"," ", " ")
    print(Restaurant2.restaurant_name)
    print(Restaurant2.cuisine_type)

    Restaurant2.describe_restaurant()
    Restaurant2.open_restaurant()

p1(), p2(), p3()

