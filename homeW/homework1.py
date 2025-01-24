class Hero:
    def __init__(self, name, lvl=10, hp=100):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def __str__(self):
        return

    def introduce(self):
        return print(f"Привет меня зовут {self.name},"
                     f" мне {self.lvl},здоровье {self.hp}")

hero_first = Hero("zohan", 2, 99)
hero_second = Hero("tor", 99,999)

    #   lvl = int(input("Введите уровень героя:"))
    #   is_adult = lvl == 10
    #   print(is_adult)
print(hero_first.introduce())
print(hero_second.introduce())