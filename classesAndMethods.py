# Python OOP
class Employee:

    num_of_emps = 0
    raise_amnt = 1.04

    def __init__ (self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amnt)

    @classmethod
    def set_raise_amnt(cls, amount):
        cls.raise_amnt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        pass


class Developer(Employee):
    raise_amnt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


emp1 = Employee('Corey', 'Schafer', 5000)

# print(Employee.raise_amnt)
# print(emp1.raise_amnt)

emp_str1 = 'abhi-sing-70000'
new_emp1 = Employee.from_string(emp_str1)
# print(new_emp1.email)

# dev1 = Developer('Corey', 'Schafer', 6000, 'python-3')
# print(dev1.email)
# print(dev1.prog_lang)


import os
import datetime
import logging


class Logging:

    logs_path = os.path.join(os.path.abspath(''), 'logs')
    file_name_path = 'logs' + "_" + datetime.datetime.now().strftime('%Y%m%d-%H%M%S') + '.txt'
    file_name = os.path.join(logs_path, file_name_path)
    logging.basicConfig(filename=file_name, filemode='w', format='%(asctime)s - %(message)s',
                        datefmt='%d-%m-%y %H:%M:%S', level=logging.INFO)
    logger = logging

    # def __init__(self):
    #     self.logs_path = os.path.join(os.path.abspath(''), 'resources', 'logs')

    # @property
    # def logger(self):
    #     file_name_path = 'logs' + "_" + datetime.datetime.now().strftime('%Y%m%d-%H%M%S') + '.txt'
    #     file_name = os.path.join(self.logs_path, file_name_path)
    #     logging.basicConfig(filename=file_name, filemode='w', format='%(asctime)s - %(message)s',
    #                         datefmt='%d-%m-%y %H:%M:%S', level=logging.INFO)
    #     return logging
    #
    # @classmethod
    # def write_logs(cls):
    #     file_name_path = 'logs' + "_" + datetime.datetime.now().strftime('%Y%m%d-%H%M%S') + '.txt'
    #     file_name = os.path.join(cls.logs_path, file_name_path)
    #     logging.basicConfig(filename=file_name, filemode='w', format='%(asctime)s - %(message)s',
    #                         datefmt='%d-%m-%y %H:%M:%S', level=logging.INFO)
    #     return logging


# logg = Logging()
# print(Logging.logs_path)
# # Logger.write_logs('Logging started!')
# Logging.logger.info('Process started!')
# Logging.logger.error('Ran into an error!')
