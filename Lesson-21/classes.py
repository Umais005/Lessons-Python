from collections import Counter
import math


class statistics:
    def __init__(self, lst: list):
        self.lst = lst

    def count(self):
        return len(self.lst)

    def sum(self):
        return sum(self.lst)

    def min(self):
        return min(self.lst)

    def max(self):
        return max(self.lst)

    def range(self):
        return self.max()-self.min()

    def mean(self):
        m = self.sum() / len(self.lst)
        return m

    def median(self):
        _sort = sorted(self.lst)
        if len(self.lst) % 2 != 0:
            return _sort[(len(self.lst)//2)+1]

        else:
            m = (_sort[(len(self.lst)//2)]+_sort[(len(self.lst)//2)+1])//2
            return m

    def mode(self):
        count = Counter(self.lst)
        return count.most_common(1)[0][0]

    def var(self):
        variance = sum((x-self.mean())**2 for x in self.lst)/self.count()
        return round(variance, 1)

    def std(self):
        return round(math.sqrt(self.var()), 1)

    def freq_dist(self):
        frequency = {}
        for i in self.lst:
            frequency[i] = frequency.get(i, 0)+1
            n = self.count()
        frq = [(f/n*100, j) for j, f in frequency.items()]
        frq.sort(reverse=True)
        return frq

    def describe(self):
        summary = (
            f"Count: {self.count()}\n"
            f"Sum:  {self.sum()}\n"
            f"Min:  {self.min()}\n"
            f"Max:  {self.max()}\n"
            f"Range:  {self.range()}\n"
            f"Mean:  {self.mean()}\n"
            f"Median:  {self.median()}\n"
            f"Mode:  {self.mode()}\n"
            f"Variance:  {self.var()}\n"
            f"Standard Deviation:  {self.std()}\n"
            f"Frequency Distribution: {self.freq_dist()}"
        )
        return summary


class PersonAccount:
    def __init__(self, f_name, l_name, incomes, exp_properties):
        self.f_name = f_name
        self.l_name = l_name
        self.incomes = incomes
        self.exp_properties = exp_properties

    def total_income(self):
        return sum(self.incomes.values())

    def total_expense(self):
        return sum(self.exp_properties.values())

    def inc_info(self):
        incomes_info = "\n".join(
            f"Income {index + 1}: {amount}"
            for index, amount in enumerate(self.incomes.values())
        )
        return incomes_info

    def expense_info(self):
        exp = "\n".join(
            f"Expense {index}: {amount}" for index, amount in (self.exp_properties.items())
        )
        return exp

    def account_info(self):
        summary = (
            f"----Account Info----\n"
            f"First Name: {self.f_name}\n"
            f"Last Name: {self.l_name}\n"
            f"Incomes:\n{self.inc_info()}\n"
            f"Expenses:\n{self.expense_info()}"
        )
        return summary

    def add_income(self, info, amount):
        self.incomes |= {info: amount}

    def add_expense(self, info, amount):
        self.exp_properties |= {info: amount}

    def account_balance(self):
        return self.total_income()-self.total_expense()
