import unittest  # 匯入 TestCase (superclass) 所需要的 unittest 套件
import functools  # 提供 reduce 函數
import operator  # 提供 add 函數


class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency)

    def divide(self, divisor):
        return Money(self.amount / divisor, self.currency)

    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency


class Portfolio:
    def __init__(self):
        self.moneys = []

    def add(self, *moneys):
        self.moneys.extend(moneys)

    def evaluate(self, currency):
        total = functools.reduce(
            operator.add, map(lambda m: m.amount, self.moneys), 0)  # 增加累加結果的初始值
        return Money(total, currency)


class TestMoney(unittest.TestCase):  # 測試類別，必須是 unittest.TestCase 類別的子類別
    def testMultiplicationInDollars(self):  # 方法名稱必須以 test 開頭
        fiveDollars = Money(5, "USD")
        tenDollars = fiveDollars.times(2)
        self.assertEqual(tenDollars, fiveDollars.times(2))

    def testMultiplicationInEuros(self):
        tenEuros = Money(10, "EUR")
        twentyEuros = Money(20, "EUR")
        self.assertEqual(twentyEuros, tenEuros.times(2))

    def testDivision(self):
        originalMoney = Money(4002, "KRW")
        actualMoneyAfterDivision = originalMoney.divide(4)
        expectedMoneyAfterDivision = Money(1000.5, "KRW")
        self.assertEqual(expectedMoneyAfterDivision.amount,
                         actualMoneyAfterDivision.amount)

    def testAddition(self):
        fiveDollars = Money(5, "USD")
        tenDollars = Money(10, "USD")
        fifteenDollars = Money(15, "USD")
        portfolio = Portfolio()  # 宣告一個 Portfolio 物件
        portfolio.add(fiveDollars, tenDollars)  # 向此 Portfolio 物件添加多個具有相同貨幣的 Money 物件
        self.assertEqual(fifteenDollars, portfolio.evaluate("USD"))  # 以相同貨幣來評估 Portfolio


if __name__ == '__main__':
    unittest.main()
