import random


# class Hero:
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp
#         self.__random_int = random.randint(1, 3)
#
#     def attack(self):
#         print(f"{self.name} атакует врага!")
#
#     def protection(self):
#         print(f"{self.name} защищается!")
#
#     def rest(self):
#         print(f"{self.name} отдыхает!")
#
#     def get_random_int(self):
#         return self.__random_int
#
# kong = Hero("Kong", 100)
# print(kong.get_random_int())
# kong.protection()

from main import Hero


class Jester(Hero):
    def __init__(self, name, health):
        super().__init__(name, health)

    def unique_attack(self):
        print(f"{self.name} совершает уникальную клоунскую атаку!")

    def unique_scream(self):
        print(f"{self.name} кричит с уникальной клоунской интонацией!")

    def action(self):
        random_int = self.get_random_int()

        if random_int == 1:
            self.attack()
        elif random_int == 2:
            self.protection()
        elif random_int == 3:
            self.rest()

jester = Jester("Jester", 100)
jester.action()




