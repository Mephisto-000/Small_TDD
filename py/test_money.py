import unittest  # 匯入 TestCase (superclass) 所需要的 unittest 套件
from money import Money
from portfolio import Portfolio


class TestMoney(unittest.TestCase):  # 測試類別，必須是 unittest.TestCase 類別的子類別

    def testMultiplication(self):
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
