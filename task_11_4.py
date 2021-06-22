class Warehouse:
    def __init__(self):
        self.technics = {}

    def add_technic(self, equipment):
        self.technics.setdefault(equipment.type_model(), []).append(equipment)

    def extract_technic(self, name):
        if self.technics[name]:
            self.technics.setdefault(name).pop(0)


class OfficeEquipment:
    def __init__(self, model, work, year):
        self.model = model
        self.work = work
        self.year = year
        self.group = self.__class__.__name__

    def type_model(self):
        return f'{self.group}'

    def __repr__(self):
        return f'{self.model} {self.work} {self.year}'


class Printer(OfficeEquipment):
    def __init__(self, model, work, year):
        super().__init__(model, work, year)

    def __repr__(self):
        return f'{self.model} {self.work} {self.year}'

    def action(self):
        return 'Печатает'


class Scanner(OfficeEquipment):
    def __init__(self, model, work, year):
        super().__init__(model, work, year)

    def action(self):
        return 'Сканирует'


class Copier(OfficeEquipment):
    def __init__(self, model, work, year):
        super().__init__(model, work, year)

    def action(self):
        return 'Копирует'


wh = Warehouse()
scan = Scanner('Cannon-400', '200', 2020)
wh.add_technic(scan)
scan = Scanner('Canon-200', '300', 2017)
wh.add_technic(scan)
scan = Scanner('Kyocera-300', '500', 2019)
wh.add_technic(scan)
copier = Copier('Xerox-3345', '100', 2020)
wh.add_technic(copier)
printer = Printer('HP-600', '200', 2018)
wh.add_technic(printer)
print(wh.technics, '\n')

wh.extract_technic('Scanner')
print(wh.technics)
