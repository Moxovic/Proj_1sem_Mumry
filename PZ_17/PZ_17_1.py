"""
Создайте класс «Банк», который имеет атрибуты суммы денег и процентной ставки.
Добавьте методы для вычисления процентных начислений и снятия денег.
"""


class Bank:
    def __init__(self, cash, proz):
        self.cash = cash
        self.proz = proz

    def up_cash(self, c_up):
        if type(c_up) == int:
            self.cash += c_up + (c_up * self.proz / 100)
            return f'Вы положили на счет {c_up} под процентную ставку {self.proz}%. Ваш баланс: {self.cash}.'
        else:
            return 'Только цифры!'

    def down_cash(self, c_down):
        if type(c_down) == int:
            self.cash -= c_down
            return f'Вы сняли {c_down}. Ваш баланс: {self.cash}.'
        else:
            return 'Только цифры!'


b = Bank(3200, 12)
print(b.up_cash(5390))
print(b.down_cash(3240))
