class Animal:
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
