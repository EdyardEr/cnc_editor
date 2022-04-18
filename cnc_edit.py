import debag
import re


def add_table(cnc_lst, cnc_table, head):
    cnc_lst = cnc_lst[0:cnc_table['mark']] + [head] + cnc_table['operations'] + cnc_lst[cnc_table['mark']:]
    debag.setting_message(f'table added: {cnc_lst}', add_table.__name__)
    return cnc_lst


def renumber(cnc_lst, re_patterns):
    renumber_lst = []
    num = 0
    for s in cnc_lst:
        ind = re.match(re_patterns['numbering'], s)
        if ind:
            renumber_lst.append(str(num)+s[ind.end()-1:])
            num += 1
        else:
            renumber_lst.append(s)
    debag.setting_message(f'renumber finished: {renumber_lst}', renumber.__name__)
    return renumber_lst


def add_links(cnc_table):
    name = cnc_table['name']
    link = cnc_table['link']
    cnc_table['operations'] = [f"0 ; - N{i + len(link) + 1} -{s}" for i, s in zip(link, name)]
    return cnc_table
