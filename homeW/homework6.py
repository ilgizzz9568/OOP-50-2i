class Letuchie:
    def letat(self):
        print("Я летаю!")

class Puhovye:
    def perya(self):
        print("У меня мягкие перья.")

class Golosistye:
    def poyut(self):
        print("Я могу петь!")

class Sovka(Letuchie, Puhovye, Golosistye):
    def __init__(self):
        print("Сова.")


sovka = Sovka()
sovka.letat()
sovka.perya()
sovka.poyut()
