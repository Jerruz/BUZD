class Rectangle:

    def __new__(cls, *args, **kwargs):  # это констурктор класса
        print('hello from __new__')
        return super().__new__(cls)

    def __init__(self, width, height):  #  инициализатор экземпляра класса
        print('hello from __init__')
        self.widht = width
        self.height = height

    def area(self):
        return self.widht * self.widht

rect = Rectangle(10, 20)


print(rect.widht)
print(rect.widht)
print(Rectangle.area(rect))