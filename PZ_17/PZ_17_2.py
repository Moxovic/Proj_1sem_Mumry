"""
Создайте класс "Животное", который содержит информацию о виде и возрасте
животного. Создайте классы "Собака" и "Кошка", которые наследуются от класса
"Животное" и содержат информацию о породе.
"""


class Animal:
    def __init__(self, kind, age):
        self.kind = kind
        self.age = age


class Dog(Animal):
    def __init__(self, spec, kind, age):
        super().__init__(kind, age)
        self.spec = spec

    def get_info(self):
        return f'Вид: {self.kind}, возраст: {self.age}, порода: {self.spec}'


class Cat(Animal):
    def __init__(self, spec, kind, age):
        super().__init__(kind, age)
        self.spec = spec

    def get_info(self):
        return f'Вид: {self.kind}, возраст: {self.age}, порода: {self.spec}'


d = Dog('Хаски', 'Пес', '3')
print(d.get_info())

c = Cat('Сибириский кот', 'Кот', '4')
print(c.get_info())
