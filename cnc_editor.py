from parser import make_table
from filework import get_lst, write_in, pass_notepad, get_path, get_notepad_path
from cnc_edit import *

debag.setting_list = {
    'get_arg': 1, 'get_lst': 1, 'make_table': 1,
    'add_table': 1, 'renumber': 1, 'write_in': 1,
    'get_path': 1, 'pass_notepad': 1, 'get_notepad_path': 1,
    'path_homedir': 1
}

re_patterns = dict(
    name_operations=r"\d+ \*   -",
    end_program=r"\d+ M30",
    start_job=r"\d+ ; START OPERATIONS:",
    numbering=r"\d+ ",
    start_table=r"\d+ ; OPERATION LINKS:"
)

head = "0 ; OPERATION LINKS:\n"

path, extension = get_path()
#path, extension = r'C:\Users\ederm\Desktop\1YST_KORPYS.H', False

if extension:
    cnc_file = get_lst(path)
    cnc_table = make_table(cnc_file, re_patterns)
    cnc_table = add_links(cnc_table)
    cnc_file = add_table(cnc_file, cnc_table, head)
    cnc_file = renumber(cnc_file, re_patterns)
    write_in(path, cnc_file)

pass_notepad(path, get_notepad_path())




