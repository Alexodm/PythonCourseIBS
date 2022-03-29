class Animal:
    inst_counter = 0

    def __init__(self):
        self.inst_counter += 1

    def print_count():
        print(Animal.inst_counter)

    print_count = staticmethod(print_count)

    def voice(self):
        pass


class Cow(Animal):
    def voice():
        voice='Mooo'
        print(voice)


class Cat(Animal):
    def voice():
        voice='Meow'
        print(voice)


class Dog(Animal):
    def voice():
        voice = 'Wuf - Wuf'
        print(voice)


cow = Cow
cow.voice()

cat = Cat
cat.voice()

dog = Dog
dog.voice()

Animal.print_count()

