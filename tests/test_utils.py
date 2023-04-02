import pytest as pytest

from utils import refactor_date, mask_card, format_data, get_last_operations


@pytest.mark.parametrize('str_date, corr_date', [('2018-10-14T08:21:33.419441', '14.10.2018'),
                                                 ('2019-10-14T08:21:33.419441', '14.10.2019'),
                                                 ('2022-10-14T08:21:33.419441', '14.10.2022')])
def test_ref_date(str_date, corr_date):
    assert refactor_date(str_date) == corr_date


@pytest.mark.parametrize('str_card, mask', [('Maestro 4598300720424501', 'Maestro 4598 30** **** 4501'),
                                            ('Счет 43597928997568165086', 'Счет **5086'),
                                            ('Visa Gold 9447344650495960', 'Visa Gold 9447 34** **** 5960'),
                                            (None, '')])
def test_mask_card(str_card, mask):
    assert mask_card(str_card) == mask


def test_format_data():
    data = {
        "id": 633268359,
        "state": "EXECUTED",
        "date": "2019-07-12T08:11:47.735774",
        "operationAmount": {
            "amount": "2631.44",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Visa Gold 3589276410671603",
        "to": "Счет 96292138399386853355"
    }

    result = '12.07.2019 Перевод организации\nVisa Gold 3589 27** **** 1603 -> Счет **3355\n2631.44 руб.'

    assert format_data(data) == result

