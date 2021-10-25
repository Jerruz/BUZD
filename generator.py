from itertools import islice



def counter():
    i = 1
    while (i <= 10):
        yield i
        i += 1


for i in counter():
    print(i)

def my_gen(x):
    while (x > 0):
        if x % 2 == 0:
            yield 'Even'
        else:
            yield 'Odd'
        x -= 1


for i in my_gen(7):
    print(i)

def mygen():
    i = 7
    while i > 0:
        yield i
        i -= 1

print(mygen())

num1 = 10
num2 = 20



def mathOP():
    return num1 + num2
    return num1 - num2
    return num1 * num2
    return num1 / num2


print(mathOP())

num1 = 10
num2 = 20


def mathOP():
    yield num1 + num2
    yield num1 - num2
    yield num1 * num2
    yield num1 / num2


print("Printing the values:")
for i in mathOP():
    print(i)

def cube(s_list: list):
    '''Функция вощвращает кубы из списка чисел
    :param s_list: принимает на вход список'''
    for i in s_list:
        yield i ** 3


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
cb = cube(a)

# print(next(iter(cube(a))), next(iter(cube(a))), next(iter(cube(a))))  # так не работает
# print(next(iter(cube(a))), next(iter(cube(a))), next(iter(cube(a))))  # так не работает
# print(next(iter(cube(a))))  # так не работает
# print(next(iter(cube(a))))  # так не работает
# print(next(cube(a)))  # так не работает
# print(next(cb))  # а так работает
# print(next(cb))  # а так работает
# print(next(cb))  # а так работает
print(*islice(cb, 2))
print(*islice(cb, 2))
print(list(islice(cb, 2)))










