# Создайте класс "Человек", который содержит информацию о имени, возрасте и поле.
# Создайте классы "Мужчина" и "Женщина", которые наследуются от класса
# "Человек". Каждый класс должен иметь метод, который выводит информацию о
# поле объекта.
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_gender(self):
        print(f"Gender: {self.gender}")


class Man(Person):
    def __init__(self, name, age):
        super().__init__(name, age, "Male")

    def display_gender(self):
        print(f"Gender: Male")


class Woman(Person):
    def __init__(self, name, age):
        super().__init__(name, age, "Female")

    def display_gender(self):
        print(f"Gender: Female")


person1 = Person("Alex", 30, "Male")
person1.display_gender()

man1 = Man("John", 25)
man1.display_gender()

woman1 = Woman("Anna", 35)
woman1.display_gender()