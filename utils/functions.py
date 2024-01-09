import json


def get_five_operation(operations):
    with open(operations, encoding='utf-8') as f:
        list_operations = json.load(f)
        five_last_operations = list_operations[-5:]
        five_last_operations.reverse()
        return five_last_operations


def grouper_card(num):
    list_ = []
    for i in range(0, 16):
        if i < 6 or i > 11:
            list_.append(num[i])
            if i == 3:
                list_.append(' ')
        else:
            list_.append('*')
            if i == 7 or i == 11:
                list_.append(' ')
    return ''.join(list_)


def grouper_account(num):
    list_ = []
    for i in range(0, 20):
        if 16 > i > 13:
            list_.append('*')
        elif i > 15:
            list_.append(num[i])
    return ''.join(list_)


def get_date_revers(operation):
    date_ = (operation['date'].split('T'))[0].split('-')
    date_.reverse()
    return '.'.join(date_)


def get_from_and_to(operation):
    to_num = operation['to'].split()[-1]
    if len(to_num) == 20:
        to_num_hide = grouper_account(to_num)
    else:
        to_num_hide = grouper_card(to_num)
    to_name = ' '.join(operation['to'].split()[:-1])
    if len(operation) > 6:
        from_num = operation['from'].split()[-1]
        if len(from_num) == 20:
            from_num_hide = grouper_account(from_num)
        else:
            from_num_hide = grouper_card(from_num)
        from_name = ' '.join(operation['from'].split()[:-1])
        return [from_name, from_num_hide, to_num_hide, to_name]
    return [0, 0, to_num_hide, to_name]


