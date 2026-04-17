'''
Class Dish and Cookbook to manage dishes.
'''

class Dish:
    def __init__(self, did, name, ing, inst):
        self.did = did
        self.name = name
        self.ing = ing
        self.inst = inst

class Cookbook:
    def __init__(self):
        self.dishes = []
    def add(self, dish):
        self.dishes.append(dish)
    def show(self):
        for d in self.dishes:
            print(d.name, "-", d.ing)

cb = Cookbook()
cb.add(Dish(1, "Momo", "Meat, flour", "Steam 15 min"))
cb.add(Dish(2, "Pasta", "Pasta, sauce", "Boil and mix"))
cb.show()
