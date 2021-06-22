class CheckListNumbers(Exception):
    @staticmethod
    def check_number(number):
        try:
            if number.isdigit():
                return number
            else:
                raise TypeError
        except TypeError:
            print('Error!')


list_item = []
cls = CheckListNumbers()
while True:
    num = input('Введите элемент списка: ')
    if num == 'stop':
        print(list_item)
        break
    if cls.check_number(num):
        list_item.append(cls.check_number(num))




