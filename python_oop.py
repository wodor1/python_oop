# első feladat

class SpaceShip:
    def __init__(self):
        self.fuel = 400
        self.passengers = ["John", "Steve", "Sam", "Danielle"]
        self.shields = True
        self.speedometer = 0

    def list_passengers(self):
        for passenger in self.passengers:
            print(f"Passenger: {passenger}")

    def add_passenger(self, new_passenger):
        self.passengers.append(new_passenger)
        print(f"{new_passenger} was added to the ship")

    def travel(self, distance):
        print(f"trying to travel: {distance}")
        if self.fuel == 0:
            print("can't go further, tank is empty")
            return
        self.fuel -= distance / 2
        if self.fuel < 0:
            actual_distance = distance + self.fuel * 2
            print(f"can only travel: {actual_distance}")
            self.speedometer += actual_distance
            self.fuel = 0
        else:
            self.speedometer += distance
        if self.fuel < 30:
            self.shields = False
            print("fuel is low, turning off shields...")
        print(f"the SpaceShip is at: {self.speedometer}")
        print(f"the spaceship has: {self.fuel} fuel")


mySpaceShip = SpaceShip()

mySpaceShip.list_passengers()
mySpaceShip.add_passenger('Lindsay')
mySpaceShip.list_passengers()
mySpaceShip.travel(750)
mySpaceShip.travel(200)
mySpaceShip.travel(100)


# második feladat

import uuid
from operator import attrgetter

class Product:
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price
        self.id = self.get_id()

    def __repr__(self):
        return f"Product(product_name='{self.product_name}', price={self.price})"

    @staticmethod
    def get_id():
        return str(uuid.uuid4()).split('-')[-1]


class Warehouse:
    def __init__(self):
        self.products = []

    def add_product(self, product_name, price):
        if not any(product.product_name == product_name for product in self.products):
            self.products.append(Product(product_name, price))

    def remove_product(self, product_name):
        self.products = [product for product in self.products if product.product_name != product_name]

    def display_products(self):
        for product in self.products:
            print(f"{product.id}, {product.product_name}, {product.price}")

    def sort_by_price(self, ascending=True):
        return sorted(self.products, key=attrgetter('price'), reverse=not ascending)


warehouse = Warehouse()
warehouse.add_product('Laptop', 3900.0)
warehouse.add_product('Mobile Phone', 1990.0)
warehouse.add_product('Camera', 2900.0)
warehouse.add_product('USB Cable', 24.9)
warehouse.add_product('Mouse', 49.0)
for product in warehouse.sort_by_price():
    print(product)
