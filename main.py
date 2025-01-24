from abc import ABC, abstractmethod
import random


class Hero(ABC):
    def __init__(self, name, health):
        self.name = name  # Имя героя
        self.health = health  # Здоровье героя
        self.__random_int = random.randint(1, 3)  # Приватный атрибут для случайного числа

    def attack(self):
        print(f"{self.name} атакует врага!")

    def protection(self):
        print(f"{self.name} защищается!")

    def rest(self):
        print(f"{self.name} отдыхает!")

    def get_random_int(self):
        return self.__random_int

    @abstractmethod
    def unique_attack(self):
        pass

    @abstractmethod
    def unique_scream(self):
        pass

    @abstractmethod
    def action(self):
        pass
