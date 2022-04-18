import debag


def get_lst(path):
    str_lst = []
    try:
        with open(path) as file:
            str_lst = file.readlines()
            debag.setting_message(f'list received: {str_lst}', get_lst.__name__)
    except FileNotFoundError:
        debag.critical_error('ERROR, path file is missing!')
    return str_lst


def write_in(path, lst):
    try:
        with open(path, 'w') as file:
            for s in lst:
                file.write(s)
            debag.setting_message(f'file is overwritten: {lst}', write_in.__name__)
    except FileNotFoundError:
        debag.critical_error('ERROR, path file is missing!')