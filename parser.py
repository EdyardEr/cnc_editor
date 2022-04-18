import re
import debag


def make_table(str_lst, re_pattern):
    table = dict(name=[], link=[], mark=0)
    start = True
    num_string = -1
    for s in str_lst:
        num_string += 1
        if start:  # search startpoint
            if re.match(re_pattern['start_table'], s):
                debag.critical_error('ERROR, already added table!')
            if re.match(re_pattern['start_job'], s):
                table['mark'] = num_string
                debag.setting_message(f'found the starting mark: {s}', make_table.__name__)
                start = False
            continue

        name = re.match(re_pattern['name_operations'], s)
        if name:  # search operation names
            table['name'].append(s[name.end():])  # f'0 ; - N{s[name.end():]}'
            table['link'].append(int(s[:name.end() - 6]))
            debag.setting_message(f'found operation: {s}', make_table.__name__)
            continue

        if re.match(re_pattern['end_program'], s):
            debag.setting_message(f'found end cnc program: {s}', make_table.__name__)
            break
    else:
        debag.critical_error('ERROR, broken file! don\'t found cnc program end!')

    debag.setting_message(f'made table: {table}', make_table.__name__)
    return table
