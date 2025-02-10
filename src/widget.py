from src.mask import get_mask_account, get_mask_card_number


def mask_account_card(type_and_number):
    '''возвращает замаскированный номер'''
    if type_and_number[:4] == 'Счет':
        return 'Счет ' + get_mask_account(type_and_number[:20])
    else:
        return type_and_number[:-16] + get_mask_card_number(type_and_number[16:])


def get_date(full_format):
    '''возвращает дату в нужном формате'''
    return full_format[8:10] + '.' + full_format[5:7] + '.' + full_format[:4]