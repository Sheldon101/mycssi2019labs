# class Pet(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# my_pet = Pet("F", 3)
# my_pet2 = Pet("D", 5)
# my_pet3 = Pet("J", 2)
# print("My pet %s is %s years old" % (my_pet.name, my_pet.age))
# print("My pet %s is %s years old" % (my_pet2.name, my_pet2.age))
# print("My pet %s is %s years old" % (my_pet3.name, my_pet3.age))
class Pet(object):
    def __init__(self, name, age, animal):
        self.name = name
        self.age = age
        self.animal = animal
        self.is_hungry = False
        self.mood = "happy"
    def eat(self):
       print("> %s is eating..." % self.name)
       if self.is_hungry:
           self.is_hungry = False
       else:
           print("> %s may have eaten too much" % self.name)
           self.mood = "lethargic"

my_pet = Pet("F",3, "dog")
my_pet.is_hungry = True
print("Is my pet hungry? %s" % my_pet.is_hungry)
my_pet.eat()
print("How about now %s" % my_pet.is_hungry)
print("My pet is feeling %s" % my_pet.mood)
