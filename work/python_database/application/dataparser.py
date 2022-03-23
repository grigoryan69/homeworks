#!/usr/bin/env python3
import re
import json

json_data = 'data.json'


def save(what):
    with open(json_data, 'w') as files:
        json.dump(what, files, indent=4)


def read():
    with open(json_data) as files:
        global loader
        loader = json.load(files)


def empty():
    try:
        read()
    except Exception:
        base = {"People": {"managers": [], "employees": [], "guests": []}}
        save(base)
        read()


def parsing():
    with open('data.txt', 'r') as fn:
        global y
        y = fn.readlines()

    find_list = []
    for i in y:
        g = i[i.find(":") + 1:]
        find_list.append(g[:-1])

    find_list = list(((v.replace(' ', '')) for v in find_list))

    try:
        ooo = 0
        for some in range(len(find_list) // 7):
            tessss = find_list[ooo:]
            if re.match('managers', tessss[0]):
                parss_dic = {'name': tessss[1], 'surname': tessss[2], 'username': tessss[3], 'password': tessss[4],
                             'email': tessss[5], 'salary': tessss[6], 'Reporters': {}}
                if parss_dic not in loader['People']['managers']:
                    loader['People']['managers'].append(parss_dic)
                save(loader)
                ooo += 9

            if re.match('employees', tessss[0]):
                parss_dic = {'name': tessss[1], 'surname': tessss[2], 'username': tessss[3], 'password': tessss[4],
                             'email': tessss[5], 'salary': tessss[6], 'manager': ''}
                if parss_dic not in loader['People']['employees']:
                    loader['People']['employees'].append(parss_dic)
                save(loader)
                ooo += 9

            if re.match('guests', tessss[0]):
                parss_dic = {'name': tessss[1], 'surname': tessss[2], 'username': tessss[3], 'password': tessss[4],
                             'email': tessss[5]}
                if parss_dic not in loader['People']['guests']:
                    loader['People']['guests'].append(parss_dic)
                save(loader)
                ooo += 7

    except IndexError:
        pass


def main():
    empty()
    parsing()


if __name__ == '__main__':
    main()
