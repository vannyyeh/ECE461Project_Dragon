import pymongo
import databaseModule


class Database:

    # Initialization Begins
    def __init__(self):

        self.__accounts = {}
        self.__hardwareSets = {}
        self.__projectList = {}

    # Initialization End
    # User Dictionary Manipulation Begin

    def add_user(self, user):

        if self.user_existence(user):
            return False
        else:
            self.__accounts[user.get_userID()] = user

    def user_existence(self, user):

        if user.get_userID() in self.__accounts.keys():
            return True
        else:
            return False

    def find_user(self, user):

        if self.user_existence(user):
            return self.__accounts.get(user.get_userID())
        else:
            return False

    def delete_user(self, user):

        if self.user_existence(user):
            del self.__accounts[user.get_userID()]
        else:
            return False

    def get_user(self, userID):

        try:
            user = self.__accounts[userID]
            return user
        except KeyError:
            return False

    def get_accounts(self):
        return self.__accounts

    # User Dictionary Manipulation End
    # HardwareSet Dictionary Manipulation Begin

    def add_hardware_set(self, hardwareSet):

        if self.hardware_set_existence(hardwareSet):
            return False
        else:
            self.__hardwareSets[hardwareSet.get_hw_name()] = hardwareSet

    def hardware_set_existence(self, hardwareSet):

        if hardwareSet.get_hw_name() in self.__hardwareSets.keys():
            return True
        else:
            return False

    def find_hardware_set(self, hardwareSet):

        if self.hardware_set_existence(hardwareSet):
            return self.__hardwareSets.get(hardwareSet.get_hw_name())
        else:
            return False

    def delete_hardware_set(self, hardwareSet):

        if self.hardware_set_existence(hardwareSet):
            del self.__hardwareSets[hardwareSet.get_hw_name()]
        else:
            return False

    def get_hardware_set(self, name):

        try:
            hardwareSet = self.__hardwareSets[name]
            return hardwareSet
        except KeyError:
            return False

    def get_all_hardware_sets(self):
        return self.__hardwareSets

    # HardwareSet Dictionary Manipulation End
    # Project Dictionary Manipulation Begin

    def add_project(self, project):

        if self.project_existence(project):
            return False
        else:
            self.__projectList[project.get_projectID()] = project

    def project_existence(self, project):

        if project.get_projectID() in self.__projectList.keys():
            return True
        else:
            return False

    def find_project(self, project):

        if self.project_existence(project):
            return self.__projectList.get(project.get_projectID())
        else:
            return False

    def delete_project(self, project):

        if self.project_existence(project):
            del self.__projectList[project.get_projectID()]
        else:
            return False

    def get_project(self, projectID):

        try:
            project = self.__projectList[projectID]
            return project
        except KeyError:
            return False

    def get_project_lists(self):
        return self.__projectList
