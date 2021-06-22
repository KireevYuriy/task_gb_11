class Data:

    @classmethod
    def date_int(cls, data_str):

        try:
            day, month, year = data_str.split('-')
            if day.isdigit() or month.isdigit() or year.isdigit():
                day = int(day)
                month = int(month)
                year = int(year)
            return day, month, year
        except Exception:
            return 'Error!'

    @staticmethod
    def check_data(day, month, year):
        if day > 31 or month > 12:
            return 'Error'
        else:
            return f'{day}.{month}.{year}'


dmy = Data()
dd, mm, yyyy = dmy.date_int('20-06-2021')
print(dmy.check_data(dd, mm, yyyy))
