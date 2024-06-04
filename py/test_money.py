import unittest  # 匯入 TestCase (superclass) 所需要的 unittest 套件


class Dollar:
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)


class TestMoney(unittest.TestCase):  # 測試類別，必須是 unittest.TestCase 類別的子類別
    def testMultiplication(self):  # 方法名稱必須以 test 開頭
        fiver = Dollar(5)
        tenner = fiver.times(2)
        self.assertEqual(10, tenner.amount)


if __name__ == '__main__':
    unittest.main()
