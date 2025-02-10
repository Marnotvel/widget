def get_mask_card_number(card_number: int) -> str:
    '''возвращает замаскированный номер карты'''
    str_card_number = str(card_number)
    return f"{str_card_number[:4]} {str_card_number[4:6]}** **** {str_card_number[-4:]}"


def get_mask_account(mask_account: int) -> str:
    '''возвращает замаскированный номер счета'''
    str_mask_account = str(mask_account)
    return f"**{str_mask_account[-4:]}"


