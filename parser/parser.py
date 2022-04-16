import re

name_operations = r"\d+ \*   -"
end_program = r"\d+ M30"
start_job = r"\d+ ; START OPERATIONS:"
numbering = r"\d+ "
start_table = r"\d+ ; OPERATION LINKS:"
operations_list = []
link_list = []
ind_start_table = False


def count_link():
    return [f"0 ; - N{i+len(link_list)+1} -{s}" for i, s in zip(link_list, operations_list)]


def discover_name(s, num_string):
    answer = re.match(name_operations, s)
    if answer:
        operations_list.append(s[answer.end():])
        link_list.append(int(s[:answer.end()-6]))
        return True


def some_func(file_list):
    start = True
    num_string = -1
    for s in file_list:
        num_string += 1
        if start:
            if re.match(start_table, s):
                print("already added table")
                return False

            if re.match(start_job, s):
                global ind_start_table
                ind_start_table = num_string
                #print(ind_start_table, s)
                start = False
            continue

        if discover_name(s, num_string):
            #print(s)
            continue
        if re.match(end_program, s):
            #print(s)
            return True
    else:
        print("broken file")  # сворачивание программы
        return False


def add_table(file_list):
    #print(*file_list)
    return file_list[0:ind_start_table] + ["0 ; OPERATION LINKS:\n"] + operations_list + file_list[ind_start_table:]


def renumber(file_list):
    print("renumber")
    enumerate_lst = []
    num = 0
    for s in file_list:
        #print(s)
        ind = re.match(numbering, s)
        if ind:
            enumerate_lst.append(str(num)+s[ind.end()-1:])
            num += 1
            #print(str(num)+s[ind.end()-1:])
        else:
            enumerate_lst.append(s)
    return enumerate_lst


try:
    with open(r"C:\Users\ederm\Desktop\1YST_KORPYS.H") as file:
        file_list = file.readlines()
        if some_func(file_list):
            operations_list = count_link()
            file_list = add_table(file_list)
            file_list = renumber(file_list)
except FileNotFoundError:
    print("path file is missing")

try:
    with open(file=r"C:\Users\ederm\Desktop\1YST_KORPYS.H", mode='w') as file:
        for s in file_list:
            file.write(s)
except FileNotFoundError:
    print("path file is missing")
