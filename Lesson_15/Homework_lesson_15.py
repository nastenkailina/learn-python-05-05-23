def generator_fibo(n):
    """
    Генератор числа фибоначи
    """
    a = 0
    b = 1
    for i in range(n):
        yield a
        _a = b
        b = a + b
        a = _a


def word_gen(string):
    """
    Генератор который выдает по одному слову из строки
    """
    words = string.split(' ')
    for w in words:
        yield w


if __name__ == '__main__':
    print(list(generator_fibo(10)))

    for word in word_gen('i am generating words from text'):
        print(word)
