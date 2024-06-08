import functools  # 提供 reduce 函數
import operator  # 提供 add 函數
from money import Money


class Portfolio:
    def __init__(self):
        self.moneys = []

    def add(self, *moneys):
        self.moneys.extend(moneys)

    def evaluate(self, currency):
        total = functools.reduce(
            operator.add, map(lambda m: m.amount, self.moneys), 0)  # 增加累加結果的初始值
        return Money(total, currency)
