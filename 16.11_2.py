class Purse:

    def __init__(self, valuta, name='Unknown'):  # код выполняется, когда создается экземпляр какого-то класса
        if valuta not in ('USD', 'EUR'):
            raise ValueError
        self.__money = 0.00  # все переменные в классе - это поля или свойства, а атрибуты - это все имена.
        '''Х идет в self, навешиваем money на х. '''
        self.valuta = valuta
        self.name = name

    def info(self):
        return self.__money

    def top_up_balance(self, howmoney):
        self.money = self.__money + howmoney

    def top_down_balance(self, howmoney):
        if self.__money - howmoney < 0:
            print('недостаточно средств')
            raise ValueError('недостаточно средств')
        self.__money = self.__money - howmoney

    def __del__(self):
        print('Кошелек удален')




x = Purse('USD')
y = Purse('EUR', 'Bill')
x.top_up_balance(100)
x.money
x.info()
x.money = -200

