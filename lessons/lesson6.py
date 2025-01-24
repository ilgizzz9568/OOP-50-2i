class Animal:
    def make_sound(self):
        print("sound")

    def action(self):
        print("parent action")



class Flyable(Animal):
    def action(self):
         return print("I'm flying")


class Swimmanble(Animal):
    def action(self):
        return print("I'm swimming")

# class Voron(Flyable):
#     pass


class Duck(Flyable, Swimmanble):
    def action(self):
        super().action()
        print("krya krya")


# print(Duck.mro())