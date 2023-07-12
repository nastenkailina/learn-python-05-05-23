from .animal import Animal


class Cat(Animal):
    # init так же называют конструктором класса
    def __init__(self, name: str, age: int, say_word='Мяу-мяу'):
        """
        Класс отвечает за симуляцию животного кота
        """
        super().__init__(
            name=name,
            age=age,
            say_word=say_word,
            preferred_food={'рыбка', 'молоко'}
        )
        self.animal_type = 'Кот'

    def treat(self, hours: int) -> str:
        """
        Ухаживая за котом должное количество времени, мы получаем мурчание
        :param hours: время ухаживания
        :return: мурчание или ничего
        """
        if hours > 3:
            print(f'Вы ухаживаете за {self} {hours} часов и получаете мурчание')
            return 'мурчание'
        print(f'Вы ухаживаете за {self} {hours} часов.')
        return ''
