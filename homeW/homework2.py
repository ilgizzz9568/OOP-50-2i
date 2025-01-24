import random


class Heroes:

    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def action(self):
        return print(f"поднимает щит {self.name}")
    def attack(self):
        return print(f"удар копьем {self.name}")

# Motoyasu = Heroes("Motoyasu", 100)
# Motoyasu.attack()


class Archer(Heroes):

    def __init__(self, name, hp, arrows, accuracy):
        super().__init__(name, hp)
        self.arrows = arrows
        self.accuracy = accuracy
    def attack(self):
        if self.arrows <= 0 :
            print("У вас нет стрел!")
            return

        self.arrows -= 1
        shot_result = random.randint(1, 100)
        if shot_result < self.accuracy:
            print("Атака успешна! Вы поразили цель.")
        else:
            print("Атака неудачна! Вы промахнулись.")

        print(f"Осталось стрел: {self.arrows}")

    def rest(self):
        self.arrows += 5
        print("Вы пополнили свой запас стрел на 5!")


        print(f"Теперь у вас {self.arrows} стрел.")

    def status(self):
            print(f"Имя: {self.name}")
            print(f"Здоровье: {self.hp}")
            print(f"Стрелы: {self.arrows}")
            print(f"Точность: {self.accuracy}%")


archer = Archer("Archer", 100, 5,70)
archer.attack()
archer.rest()
archer.status()

