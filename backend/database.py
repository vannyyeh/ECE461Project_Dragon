import pymongo
import databaseModule


class Database:
    def __init__(self):
        self.__accounts = []
        self.__hardwareSets = []

    def add_user(self, user):
        self.__accounts.append(user)

    def user_existence(self, user):
        return user not in self.__accounts

    def find_user(self, user):
        if self.user_existence(user):
            return self.__accounts.index(user)
        else:
            return False

    def delete_user(self, user):
        if self.user_existence(user):
            self.__accounts.remove(user)
            return True
        else:
            return False

