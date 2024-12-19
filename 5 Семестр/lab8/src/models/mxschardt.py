from datetime import date

from .user_base import UserBase


class MaximSchardt(UserBase):

    def __init__(self):
        self.__second_name = "Schardt"
        self.__first_name = "Maxim"
        self.__fathers_name = "Alexandrovich"

    def get_name(self):
        return self.__first_name
   
    def show_name(self):
        print(
            f"{self.__second_name} {self.__first_name} {self.__fathers_name}")

    def get_fullname(self):
        return {
            'first_name': self.__first_name,
            'second_name': self.__second_name,
            'fathers_name': self.__fathers_name
        }

    def get_birthday(self):
        return date(2002, 11, 2)
