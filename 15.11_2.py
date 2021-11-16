class My_class():

    @staticmethod
    def ex_static_method():  #  статический метод. Можно вызвать не создавая экземпляр класса
        print('static method')

    @classmethod  #  классовый метод. Можно вызвать не создавая экземпляр класса
    def ex_class_method(cls):
        print('class method')

    def ex_method(self):
        print('method')

My_class.ex_static_method()
My_class.ex_class_method()

m = My_class()  # создаем экземпляр класса

m.ex_method()