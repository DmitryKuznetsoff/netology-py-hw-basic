animals_dict = {}

# общий класс для всех животных
# содержит общие для всех атрибуты: name, weight, voice
# и общие для всех методы: feed, speak
class Animals:
    name = ''
    weight = 0
    voice = ''

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        # пишем пары Имя: Вес в словарь для последующих манипуляций:
        animals_dict.update({self.name: self.weight})

    def feed(self):
        return print('omnomnom')

    def speak(self):
        return print(self.voice)


# отдельный класс для птиц
# содержит специфический метод get_eggs
class Birds(Animals):
    def get_eggs(self):
        return print('eggs collected')


# отдельный класс для животых, дающих молоко
# содержит специфический метод get_milk
class MilkyWay(Animals):
    def get_milk(self):
        return print('milk collected')


# создаём класс для каждого животного:
class Goose(Birds):
    # переопределяем атрибут voice для каждого животного в его классе:
    voice = 'gagaga'


class Chicken(Birds):
    voice = 'kokoko'


class Duck(Birds):
    voice = 'quack'


class Cow(MilkyWay):
    voice = 'mooooo'


class Goat(MilkyWay):
    voice = 'beeeee'


class Sheep(Animals):
    voice = 'meeeee'

    def get_wool(self):
        return print('wool collected')


# создаём объекты животных для каждого класса
# с указанием атрибутов self.name и self.weight:
goose0 = Goose('Серый', 3)
goose1 = Goose('Белый', 2.8)
cow0 = Cow('Манька', 700)
sheep0 = Sheep('Барашек', 70)
sheep1 = Sheep('Кудрявый', 65)
chicken0 = Chicken('Ко-Ко', 2)
chicken1 = Chicken('Кукареку', 2.5)
goat0 = Goat('Рога', 80)
goat1 = Goat('Копыта', 90)
duck0 = Duck('Кряква', 4)

# cow0.speak()
# cow0.feed()
# cow0.get_milk()

# считаем общий вес животных, суммируя values словаря:
total_weight = sum(list(animals_dict.values()))
print('общий вес всех животных на ферме: ', total_weight)
# находим животное с максималаьным весом и выводим его:
max_weight = max(animals_dict, key=animals_dict.get)
print('самое тяжёлое животное на ферме: ', max_weight)
