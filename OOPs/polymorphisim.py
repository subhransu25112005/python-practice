class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


class Cat(Animal):
    def sound(self):
        print("Cat meows")


def make_sound(animal):
    animal.sound()   # same method, different output


def main():
    dog = Dog()
    cat = Cat()

    make_sound(dog)
    make_sound(cat)


if __name__ == "__main__":
    main()
