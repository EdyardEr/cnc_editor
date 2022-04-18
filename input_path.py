import sys
import debag


def get_path():
    """
    :return: path of uploaded file
    """
    if len(sys.argv) == 1:
        debag.critical_error('ERROR, pass the file to the program!')
    elif len(sys.argv) == 2:
        debag.setting_message(f'get attribute: {sys.argv[1]}', get_path.__name__)
        return sys.argv[1]
    else:
        debag.critical_error('ERROR, too many attributes!')