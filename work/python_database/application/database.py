#!/usr/bin/env python
import json
import random
import dataparser
from signal import signal, SIGINT
from sys import exit
import re
import os

json_data = 'data.json'


def handler(SIGINT, handler):
    print('CTRL-C detected. Exiting the program')
    exit(0)


def dump_to_json(what):
    with open(json_data, 'w') as files:
        json.dump(what, files, indent=4)


def load_from_json():
    with open(json_data) as files:
        return json.load(files)


def json_basic_structure():
    base = {"People": {"managers": [], "employees": [], "guests": []}}
    dump_to_json(base)
    dataparser.main()


def check_if_json_exists(file_name) -> bool:
    # Check if file exist or not
    return os.path.exists(file_name)


def create_empty_json():
    if not check_if_json_exists(json_data):
        open(json_data, 'w')


def empty():
    check_file = os.stat(json_data).st_size
    if check_file == 0:
        json_basic_structure()
    else:
        with open(json_data) as files:
            json.load(files)


# Function to check if name or surname contains an integer if


def contains_number(value):
    for character in value:
        if character.isdigit():
            return True
    return False


# Class to raise when name or surname contains an integer if


class NotValidInput(Exception):
    pass


# Created a class to raise a massage when value of salary les then 0


class SalaryError(Exception):
    pass


# My class Parent of parents : )


class Person:

    def __init__(self, role, name, surname, username, email, password):
        self.role = role
        if len(name) > 0 and len(surname) > 0:
            if not contains_number(name) and not contains_number(surname):
                self.name = name
                self.surname = surname
            else:
                raise NotValidInput('You cant use numbers in name \
                    and surname pool. ')
        if not email[-10:] == '@gmail.com' or email[-8:] == '@mail.ru' \
                or email[-10:] == '@yandex.ru':
            raise NotValidInput("Your email is incorrect")
        else:
            self._email = email
        if username == '' or password == '':
            raise TypeError('Don\'t press enter')
        else:
            self._username = username
            self._password = password

    # method to get username
    def get_username(self):
        return self._username

    # method to set username
    def set_username(self, username):
        self._username = username

    # method to get password
    def get_password(self):
        return self._password

    # method to set password
    def set_password(self, password):
        self._password = password

    # method to get everything that has guest
    def everything(self):
        return self.role, self.name, self.surname, \
               self._username, self._email, self._password


class Guest(Person):
    def __init__(self, role, name, surname, username, email, password):
        super().__init__(role, name, surname, username, email, password)


class Short(Person):
    def __init__(self, role, name, surname, username, email, password):
        super().__init__(role, name, surname, username, email, password)


class Manager(Short):

    def __init__(self, role, name, surname, username, email, password, manager_salary):
        super().__init__(role, name, surname, username, email, password)
        self._salary = manager_salary

    def set_salary(self, manager_salary):
        self._salary = manager_salary

    def get_salary(self):
        return self._salary

    def everything(self):
        return self.role, self.name, self.surname, self._username, \
               self._email, self._password, self._salary


class Employee(Short):
    def __init__(self, role, name, surname, username, email, password, employee_salary):
        super().__init__(role, name, surname, username, email, password)
        self._salary = employee_salary

    def get_salary(self):  # get salary of manager
        return self._salary

    def everything(self):
        return (self.role, self.name, self.surname, self._username,
                self._email, self._password, self._salary)


# *********************Registration,login,Login_inputs[Functions]******************


count_manager = 0
count_employee = 0
count_guest = 0

guests_usernames_lists = []
employees_usernames_lists = []
managers_usernames_lists = []

guests_password_lists = []
employees_password_lists = []
managers_password_lists = []


def read_login_and_password_from_db(role, username_in, password_in):
    loader = load_from_json()
    for i in loader['People'][role]:
        username_in.append(i['username'])
        password_in.append(i['password'])


action = ''


def correct_name(what, who):
    global action
    if contains_number(what) or what == '' or not what.istitle():
        what = input(f'{who.title()}: ')
        correct_name(what, who)
    else:
        action = what


def correct_email(emails):
    try:
        int(emails)

    except ValueError:
        global action
        regex_gmail = r'\b[A-Za-z0-9._%+-]+@gmail.com+\b'
        regex_mail_ru = r'\b[A-Za-z0-9._%+-]+@mail.ru+\b'
        regex_yandex_ru = r'\b[A-Za-z0-9._%+-]+@yandex.ru+\b'
        if not (re.fullmatch(regex_gmail, emails)) \
                and not (re.fullmatch(regex_mail_ru, emails)) \
                and not (re.fullmatch(regex_yandex_ru, emails)):
            emails = input('Email: ')
            correct_email(emails)
            return 0

        else:
            action = emails
            return action
    else:
        return 0


def input_salary():
    global salary
    salary = input('salary not less then 50 --> ')
    try:
        int(salary)
    except ValueError:
        input_salary()
        if (salary < '50') or (salary == ''):
            print(f'Salary can\'t be less then {salary}')
            input_salary()


def registration():
    reg_user = r'\b[A-Za-z0-9._]+\b'
    global count_manager, count_employee, count_guest
    role = input('ROLE = (Guest[1] Manager[2] Employee[3]): ')
    role = role.lower()
    if role == 'guest' or role == '1' or role == 'g' \
            or role == 'manager' or role == '2' or role == 'm' \
            or role == 'employee' or role == '3' or role == 'e':
        name = input('Name: ')
        correct_name(name, 'name')
        name = action
        surname = input('Surname: ')
        correct_name(surname, 'surname')
        surname = action
        username = input('Username: ')

        def correct_username_and_password(what, who):
            global action
            if not (re.fullmatch(reg_user, what)) or not len(what) > 1 \
                    or what[0].isdigit():
                what = input(f'{who.title()}: ')
                correct_username_and_password(what, who)
            else:
                action = what

        correct_username_and_password(username, 'username')
        username = action

        def if_username_exist(rule):
            database_exist = load_from_json()
            nonlocal username
            for i in range(len(database_exist['People'][rule])):
                if username in database_exist['People'][rule][i]['username']:
                    print('this username already exist')
                    username = input('Username: ')
                    if_username_exist(rule)

        if_username_exist('guests')
        if_username_exist('managers')
        if_username_exist('employees')

        email = input('Email: ')
        correct_email(email)
        email = action
        password = input('Password: ')
        correct_username_and_password(password, 'password')
        password = action
        if role == 'guest' or role == '1' or role == 'g':

            guest_user = Guest('guest', name, surname, username,
                               email, password)
            count_guest += 1
            guest_dict = {
                'name': guest_user.everything()[1],
                'surname': guest_user.everything()[2],
                'username': guest_user.everything()[3],
                'email': guest_user.everything()[4],
                'password': guest_user.everything()[5]
            }
            loader = load_from_json()
            loader['People']['guests'].append(guest_dict)
            dump_to_json(loader)

        elif role == 'employee' or role == '3' or role == 'e':

            input_salary()
            print(salary)
            employee_user = Employee('employee', name, surname, username,
                                     email, password, salary)
            count_employee += 1
            employee_dict = {'name': employee_user.everything()[1], 'surname': employee_user.everything()[2],
                             'username': employee_user.everything()[3], 'email': employee_user.everything()[4],
                             'password': employee_user.everything()[5], 'salary': employee_user.everything()[6],
                             'manager': ""}
            loader = load_from_json()
            loader['People']['employees'].append(employee_dict)
            dump_to_json(loader)

        elif role == 'manager' or role == '2' or role == 'm':

            input_salary()
            manager_user = Manager('manager', name, surname, username,
                                   email, password, salary)
            count_manager += 1
            manager_dict = {'name': manager_user.everything()[1], 'surname': manager_user.everything()[2],
                            'username': manager_user.everything()[3], 'email': manager_user.everything()[4],
                            'password': manager_user.everything()[5], 'salary': manager_user.everything()[6],
                            'Reporters': {}}
            loader = load_from_json()
            loader['People']['managers'].append(manager_dict)
            dump_to_json(loader)
    else:
        print('\nWe have only 3 options\n')
        print('Guest[1, g, guest]')
        print('Manager[2, m, or manager]')
        print('Employee[3, e or employee]')
        registration()


def divide_employees_into_managers():
    load_from_json()
    users_info = load_from_json()
    employees = users_info["People"]['employees']
    managers = users_info["People"]['managers']
    index = 0
    for employee in employees:
        manager_index = random.randint(0, len(managers) - 1)
        if len(employee["manager"]) == 0:
            managers[manager_index]["Reporters"].update({
                f"employee-{index + 1}": employee["username"]
            })
            employees[index].update({
                "manager": managers[manager_index]["username"]
            })
            dump_to_json(users_info)
        index += 1


def guest_info(roles):
    guest_loader = load_from_json()
    for i in guest_loader['People'][roles]:
        for key, value in i.items():
            print(f'{key.title()} --?> {value}')


def change_guest_staff(roles, us_ps, uspas):
    global change
    loader = load_from_json()
    change = input(f'enter guest {us_ps}: ')
    if change in uspas:
        guest_new_username = input(f'Enter new {us_ps} for {change}: ')
        this = loader['People'][roles]
        for x in this:
            for _, _ in x.items():
                this[uspas.index(change)][us_ps] = guest_new_username
                dump_to_json(loader)
                break


def login_check(role, can_do, base_can_type, whose_usernames_lists,
                whose_password_lists):
    loader = load_from_json()
    for i in range(len(loader['People'][role])):
        if whose_usernames_lists[i] == login_username \
                and whose_password_lists[i] == login_password \
                or loader['People'][role][i]['username'] == login_username \
                and loader['People'][role][i]['password'] == login_password:
            print(f'\n{role} Success!')
            print(f'{can_do}')
            to_do = input(f'just type {base_can_type}: ')
            print()
            try:
                to_do = int(to_do)
            except ValueError:
                print(f'you can type only {base_can_type}')
            else:
                the_guest = loader['People'][role][i]
                if to_do == 1:
                    print(f"username --> {the_guest['username']}")
                elif to_do == 2:
                    print(f"password --> {the_guest['password']}")

                elif to_do == 3:
                    new_username = input('Enter your new username: ')
                    the_guest['username'] = new_username
                    dump_to_json(loader)

                elif to_do == 4:
                    new_password = input('Enter your new password: ')
                    the_guest['password'] = new_password
                    dump_to_json(loader)

                elif to_do == 5:
                    if role == 'employees':
                        print('guests list\n')
                        guest_info('guests')

                    elif role == 'managers':
                        print('employees list\n')
                        guest_info('guests')

                elif to_do == 6:
                    if role == 'employees':
                        change_guest_staff('guests', 'username',
                                           guests_usernames_lists)
                    elif role == 'managers':
                        change_guest_staff('guests', 'username',
                                           guests_usernames_lists)
                elif to_do == 7:
                    if role == 'employees':
                        change_guest_staff('guests', 'password',
                                           guests_password_lists)
                    elif role == 'managers':
                        change_guest_staff('guests', 'password',
                                           guests_password_lists)
                else:
                    print('Incorrect input')


def check_inputs():
    global login_username, login_password
    login_username = input('Enter your username: ')
    login_password = input('Enter your password: ')
    return login_username, login_password


# ********************************Reg/login**********************************


def choose_mode():
    global mode
    mode = input('login/Registration: ')
    if mode == 'login' or mode == 'log' or mode == '1' or mode == 'l':
        print()
        load_from_json()
        check_inputs()
    elif mode == 'reg' or mode == 'registration' or mode == '2' or mode == 'r':
        print()
        for i in range(3):
            registration()
        divide_employees_into_managers()
        check_inputs()
    elif mode == 'exit' or mode == 'close' or mode == '^c':
        exit()
    else:
        choose_mode()


def choose_login_or_registration():
    try:
        choose_mode()
    except KeyboardInterrupt:
        print()
        print('Press Ctrl c to close the app')
        signal(SIGINT, handler)
        choose_login_or_registration()


# ********************************Login_inputs_call****************************


def go_login():
    divide_employees_into_managers()
    base_can_do = '\nChoose some option \n\
    [get_username[1]]\n\
    [get_password[2]]\n\
    [set_username[3]]\n\
    [set_password[4]]\n'
    employee_can_do = '[get_guests[5]]\n\
    [change_guest_username[6]]\n\
    [change_guest_password[7]]\n'
    employee_can_do = base_can_do + employee_can_do

    manager_can_do = employee_can_do
    while True:
        try:
            login_check('guests', base_can_do, '1 2 3 or 4',
                        guests_usernames_lists, guests_password_lists)
            login_check('employees', employee_can_do, '1 2 3 4 5 6 or 7',
                        employees_usernames_lists, employees_password_lists)
            login_check('managers', manager_can_do, '1 2 3 4 5 6 7',
                        managers_usernames_lists, managers_password_lists)
        except KeyboardInterrupt:
            try:
                check_inputs()
            except KeyboardInterrupt:
                choose_login_or_registration()


def main():
    create_empty_json()
    empty()
    read_login_and_password_from_db('guests', guests_usernames_lists, guests_password_lists)
    read_login_and_password_from_db('employees', employees_usernames_lists, employees_password_lists)
    read_login_and_password_from_db('managers', managers_usernames_lists, managers_password_lists)
    try:
        choose_login_or_registration()
    except KeyboardInterrupt:
        choose_login_or_registration()
    try:
        go_login()
    except KeyboardInterrupt:
        choose_login_or_registration()


if __name__ == '__main__':
    try:
        main()
    except EOFError:
        pass
        # Do nothing if EOFError
