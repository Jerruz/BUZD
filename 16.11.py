class Purse:

    def show(self, name='Unknown'):  # это класс. Он может создать множество объектов.
        print('hello', name)


''' это метод класса. В SELF передается имя переменной, в которой запущен класс.
        Т.е. в SELF попадет имя X. Это нужно, чтобы показать с каким объектом будет
        работать метод show()
'''

x = Purse()
y = Purse()
x.show()  # вызвали метод SHOW() объекта Х
y.show('Ben')
