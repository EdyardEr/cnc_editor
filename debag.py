from sys import exit


setting_list = []


def critical_error(mess):
    input(mess)
    exit()


def setting_message(mess, func_name=None):
    if setting_list[func_name] == True or func_name == None:
        input(mess)