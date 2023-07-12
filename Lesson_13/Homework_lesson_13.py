from random import choices, randint, random


class Cat:
    # тело класса
    def __init__(self, name: str, age: int, breed: str, preferred_food: set):
        """
        Класс кошка
        :param name: имя
        :param age: возраст
        :param breed: порода
        :param preferred_food: предпочитаемая еда
        """
        print('Создан объект класса Cat')
        self.name = name
        self.age = age
        self.breed = breed
        self.preferred_food = preferred_food

        # голодная ли кошка
        self.hungry = True
        # сколько часов гуляла
        self.hours_outdoors = 0

    def __str__(self):
        """
        вывод информации про кошку
        """
        starting_str = f"{self.breed.capitalize()} {self.name}, {self.age} "
        if self.age == 1:
            starting_str += "год"
        elif 2 <= self.age <= 4:
            starting_str += "года"
        else:
            starting_str += "лет"
        starting_str += f", часов гулял: {self.hours_outdoors}, голоден: {self.hungry}"
        return starting_str

    def meow(self, count: int):
        """
        метод мяуканья
        """
        if count > 0:
            meow_str = '-'.join(["мяв"] * count).capitalize()
            print(f"{self.name} мяукает: {meow_str}!")

    def eat(self, food: str):
        """
        метод еды
        """
        if self.hungry:
            if food in self.preferred_food:
                print(f"{self.name} кушает {food}")
                self.hungry = False
            else:
                print(f"{self.name} такое не ест: {food}")
                self.meow(randint(1, 5))
        else:
            print(f"{self.name} не голоден")

    def walk(self, alone: bool):
        """
        метод прогулки
        """
        if alone:
            hours = randint(2, 6)
            with_str = "сам"
        else:
            hours = randint(1, 3)
            with_str = "с хозяином"
        print(f"{self.name} гуляет {with_str} {hours} часов")
        self.hours_outdoors += hours
        if self.hours_outdoors > 3:
            self.hungry = True

        return "Хорошее настроение!" if not alone else "Ему грустно"

    def end_day_check(self):
        """
        проверка в конце дня кушала и гуляла ли кошка
        """
        print(self.name + ' голодый') if self.hungry else print(self.name + ' сытый')
        print(self.name + ' сегодня гулял') if self.hours_outdoors > 0 else print(self.name + ' сегодня не гулял')


if __name__ == '__main__':
    """
    создание несколько котов
    """
    cats = [
        Cat('Принц', 1, "британец", {'риба', 'молоко', 'каша'}),
        Cat('Персик', 4, "шотландец", {'броколли', 'йогурт'}),
        Cat('Ричард', 7, "сиамский", {'мясо', 'йогурт'}),
        Cat('Смайлик', 11, "бенгальский", {'каша', 'молоко'}),
        Cat('Матильда', 5, "сфинкс", {'молоко', 'молоко'}),
        Cat('Боцман', 4, "мейн-кун", {'йогурт', 'каша'})
    ]

    potential_food = ['риба', 'броколли', 'мясо', 'каша', 'йогурт', 'молоко']

    """
    типичный день кошки
    """
    for cat in cats:
        events_for_cat = randint(1, 8)

        for _ in range(events_for_cat):
            if random() > 0.5:
                print(f'Кормим {cat.name}')
                for random_food in choices(potential_food, k=3):
                    cat.eat(random_food)
            else:
                if random() > 0.5:
                    result = cat.walk(alone=True)
                else:
                    result = cat.walk(alone=False)
                print(f'После прогулки хозяин понял, что: {result}')
        cat.end_day_check()
        print(f'Прошел день для: {cat.name}')
        print('=' * 20)
