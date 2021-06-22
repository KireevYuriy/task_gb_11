class Division(Exception):
    def __init__(self, number_one, number_two):
        self.number_one = number_one
        self.number_two = number_two

    def incorrect(self):
        try:
            return self.number_one / self.number_two
        except Exception:
            print("Error: Выполнить деление невозможно")


c = Division(5, 0)
print(c.incorrect(), f'- результат деления')
c = Division('f', 2)
print(c.incorrect(), f'- результат деления')
c = Division(6, 2)
print(c.incorrect(), f'- результат деления')
