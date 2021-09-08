from datetime import date

# 1 вариант по условию, а 2 с проверкой данных через date
# оставил 2
class MyDate:
    def __init__(self, date_in_list):
        self.date_in_list = date_in_list

    @classmethod
    def set_date(cls, date_in):
        return cls(tuple(map(int, date_in.split('-'))))

    @staticmethod
    def valid_date(obj):
        # --- Вариант 1
        # max_val = (31, 12, 2021)
        # res_valid = not(False in list(
        #     map(lambda i: 0 < obj.date_in_list[i] < max_val[i], range(3))))

        # --- Вариант 2
        try:
            try_valid = date(*reversed(obj.date_in_list))
        except ValueError:
            res_valid = False
        else:
            res_valid = True
        finally:
            return res_valid


date_input = MyDate.set_date('10-02-1982')
print(f'{"-".join(map(str, date_input.date_in_list))} '
      f'- {MyDate.valid_date(date_input)}')

date_input = MyDate.set_date('32-02-1982')
print(f'{"-".join(map(str, date_input.date_in_list))} '
      f'- {MyDate.valid_date(date_input)}')
