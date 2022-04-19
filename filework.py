import sys
import os
import debag
import subprocess


def get_path():
    """
    :return: path of uploaded file
    """
    if len(sys.argv) == 1:
        debag.critical_error('ERROR, pass the file to the program!')
    elif len(sys.argv) == 2:
        path = sys.argv[1]
        extension = path[path.rfind('.')+1:]
        debag.setting_message(f'get attribute: {path}', get_path.__name__)
        debag.setting_message(f'get extension: {extension}', get_path.__name__)
        if extension.lower() == 'h':
            return sys.argv[1], True
        else:
            debag.setting_message(f'wrong extension!', get_path.__name__)
            return sys.argv[1], False
    else:
        debag.critical_error('ERROR, too many attributes!')


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


def pass_notepad(cnc_path, notepad_path):
    debag.setting_message(f'open file in notepad: \"{notepad_path}\" \"{cnc_path}\"', pass_notepad.__name__)
    subprocess.Popen([notepad_path, cnc_path])


def get_notepad_path():
    direct = path_homedir()
    path_notepad = f'{direct}path_notepad.txt'
    debag.setting_message(f'create path for path_notepad: {path_notepad}', get_notepad_path.__name__)
    try:
        with open(path_notepad) as file:
            path = file.readline().rstrip()
            debag.setting_message(f'accepted notepad path: {path}', get_notepad_path.__name__)
            return path
    except FileNotFoundError:
        debag.critical_error('ERROR, path_notepad file is absent!')


def path_homedir():
    path_script = sys.argv[0]
    sep = '\\'
    direct = f'{path_script[:path_script.rfind(sep) + 1]}'
    debag.setting_message(f'terminal command dir: {direct}', path_homedir.__name__)
    return direct
