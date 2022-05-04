import re
import csv
from pprint import pprint
from patterns import pattern, pattern_2, pattern_3, re_pattern, re_pattern_2, re_pattern_3, pattern_4, re_pattern_4


def open_csv():
    with open("phonebook_raw.csv") as f:
        rows = csv.reader(f, delimiter=',')
        contact_list = list(rows)
        return contact_list


def replace_name():
    result_list = []
    for i in open_csv():
        test_list = ''.join(i)
        result_list.append(re.sub(pattern, re_pattern, test_list))
    result_list_modded = []
    for j in result_list:
        result_list_modded.append(re.sub(pattern_4, re_pattern_4, j))
    return result_list_modded


def replace_tel_number():
    result_list = []
    for i in replace_name():
        result_list.append(re.sub(pattern_2, re_pattern_2, i))
    pprint(result_list)
    return result_list


def replace_add_number():
    result_list = []
    for i in replace_tel_number():
        result_list.append((re.sub(pattern_3, re_pattern_3, i)).split(','))
    pprint(result_list)
    return result_list


def replace_dublicate():
    i = 1
    result_list = replace_add_number()
    len_list = len(result_list)
    while i < len_list - 1:
        j = i + 1
        while j < len_list:
            if result_list[i][0] == result_list[j][0] and result_list[i][1] == result_list[j][1]:
                if result_list[j][2] != '':
                    result_list[i][2] = result_list[j][2]
                elif result_list[j][3] != '':
                    result_list[i][3] = result_list[j][3]
                elif result_list[j][4] != '':
                    result_list[i][4] = result_list[j][4]
                elif result_list[j][5] != '':
                    result_list[i][5] = result_list[j][5]
                elif result_list[j][6] != '':
                    result_list[i][6] = result_list[j][6]
                elif result_list[j][7] != '':
                    result_list[i][7] = result_list[j][7]
                result_list.pop(j)
                len_list -= 1
                continue
            j += 1
        i += 1
    return result_list


def load_csv():
    with open("phonebook.csv", 'w', newline='') as f:
        datawriter = csv.writer(f, delimiter=',', quotechar='|')
        for i in replace_dublicate():
            datawriter.writerow(i)


if __name__ == '__main__':
    open_csv()
    load_csv()
