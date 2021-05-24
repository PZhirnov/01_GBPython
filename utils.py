from requests import get, utils
from decimal import Decimal
from datetime import datetime

CURRENCIES_DATA = {}  # принял решение хранить словарь постоянно, чтобы потом брать нужное без повторного запроса

# Функция по условию - используется только для получения данных из словаря
# Добавлены единицы измерения, чтобы результат можно было интерпретировать корректно


def currency_rates(cur_code):
    if CURRENCIES_DATA.get(cur_code.upper()) is None:
        return None, None  #
    return CURRENCIES_DATA.get(cur_code.upper())


# Функция плучает значения по тегам


def value_tag(data_in, tag_in, tag_out="</"):
    pos_in = data_in.find(tag_in) + len(tag_in)
    pos_out = data_in.find(tag_out, pos_in)
    return data_in[pos_in:pos_out].strip()


# Функция выполняет запрос и возвращает список с предварительным разделением блоков


def response_from_url(url_in, tag_in):
    response = get(url_in)
    encodings = utils.get_encoding_from_headers(response.headers)
    content_in = response.content.decode(encoding=encodings)
    list_content = content_in.split(tag_in)
    # сразу добавляем данные в словарь
    for data_cur in list_content[1:]:
        # currencies_data[value_tag(data_cur, '<CharCode>')] = float(value_tag(data_cur, '<Value>').replace(',', '.'))
        CURRENCIES_DATA[value_tag(data_cur, '<CharCode>')] = (Decimal(value_tag(data_cur, '<Value>').replace(',', '.'))
                                                              .quantize(Decimal("1.00")),
                                                              value_tag(data_cur, '<Nominal>'))
    return list_content


# Выгружаем данные
from_response = response_from_url('http://www.cbr.ru/scripts/XML_daily.asp', "<Valute ID=")

# вытаскиваем дату из первого блока - <ValCurs Date="22.05.2021" name="Foreign Currency Market">


def date_cur():
    pos_date = from_response[0].find('Date=') + 6
    data_str = from_response[0][pos_date:pos_date + 10]
    data_str = datetime.strptime(data_str, '%d.%m.%Y').date()
    return data_str

