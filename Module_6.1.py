class  Animal:
    def __init__(self, name):
        self.alive = True #живой
        self.fed = False #накормленный
        self.name = name #индивидуальное название каждого животного

    def eat(self, food):
        self.food = food
        if food.edible:
            self.fed = True  # выжил
            print(f'{self.name} съел {food.name}') #если растение съедобное
        else: #если не съедобное
            self.alive = False  # если съел несъедобное, то погиб
            print(f'{self.name} не стал есть {food.name}') # не стал есть

class Mammal(Animal):
   pass
class Predator(Animal):
    pass
class Plant:
    def __init__(self, name):
     self.edible = False #съедобность
     self.name = name # индивидуальное название каждого растения
class Flower(Plant):
    pass
class Fruit(Plant):
    def __init__(self, name):
        self.name = name
        self.edible = True

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)


