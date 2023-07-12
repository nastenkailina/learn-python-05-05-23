class Animal:
    def __init__(self, name: str, age: int, say_word: str, preferred_food: set):
        """
        Класс отвечает за симуляцию жизнедеятельности животного на ферме
        :param name: имя животного
        :param age: возраст животного
        :param say_word: какой "фразой" животное симулирует разговор
        :param preferred_food: рацион питания
        """
        self.animal_type = '???'
        self.name = name
        self.age = age
        self.say_word = say_word
        self.preferred_food = preferred_food
        self.hungry = True
        self.visited_vet = False

    def __str__(self):
        return f'{self.animal_type} {self.name}'

    def say(self):
        """
        Животное произносит заготовленные "фразы" для привлечения внимания в чате :)
        """
        print(f'{self} говорит: {self.say_word}')

    def eat(self, food: str):
        """
        Метод отвечает за симуляцию еды у животного на ферме
        Если предложенная еда есть в preferred_food, то животное наестся и self.hungry = False
        иначе животное не покушает
        :param food: что кушаем
        """
        if not self.hungry:
            return
        if food in self.preferred_food:
            print(f'{self} кушает {food}')
            self.hungry = False
        else:
            print(f'{self} такое не ест: {food}')
            self.say()

    def treat(self, hours: int):
        """
        Метод ухаживания за животным
        :param hours: сколько часов мы проводим с животным
        :return: что получаем взамен
        """
        # подчёркивает необходимость заполнения этого метода в каждом наследнике
        raise NotImplementedError

    def visit_vet(self):
        """
        Метод посещения ветеринара
        """
        self.visited_vet = True

    def is_visited_vet(self):
        """
        Метод вывода информации о посещении ветеринара
        """
        print(self.name+' был у ветеринара, с ним все впорядке') if self.visited_vet else print(self.name + ' нужно посетить ветеринара')
