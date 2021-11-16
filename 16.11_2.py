class Purse:

    def __init__(self):  # код выполняется, когда создается экземпляр какого-то класса
        self.money = 0.00  # все переменные в классе - это поля или свойства, а атрибуты - это все имена.
        '''Х идет в self, навешиваем money на х. '''

    def info(self):
        return self.money




x = Purse()
y = Purse()
