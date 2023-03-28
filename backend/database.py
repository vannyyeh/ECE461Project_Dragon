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

    def parse_users(self, filename):
        file = open(filename, 'r')

        accounts = []

        username = ""
        userID = 0
        password = ""
        projectsArray = []

        for line in file:
            if(line != ""):
                splitLine = line.split()
                command = splitLine[0]

                if(command == ("username:")):
                    username = splitLine[1]
                if (command == ("userID:")):
                    userID = splitLine[1]
                if (command == ("password:")):
                    password = splitLine[1]
                if (command == ("projects:")):
                    projectsArray = splitLine[1].split(',')
                    parsed = databaseModule.User(username, userID, password, projectsArray)
                    accounts.append(parsed)
                    # add to the array of
        file.close()
        return accounts

    def parse_HWSets(self, filename):
        file = open(filename, 'r')

        allHW = []

        name = ""
        capacity = 0
        availability = 0
        requested = 0

        for line in file:
            if(line != ""):
                splitLine = line.split()
                command = splitLine[0]

                if(command == ("name:")):
                    name = splitLine[1]
                if (command == ("capacity:")):
                    capacity = int(splitLine[1])
                    availability = capacity
                    parsed = databaseModule.HardwareSet(name, capacity, availability, requested)
                    allHW.append(parsed)
                    # add to the array of
        file.close()
        return allHW

    def parse_projects(self, filename):
        file = open(filename, 'r')

        projectList = []

        name = ""
        desc = ""
        projectID = ""
        users = []

        for line in file:
            if(line != ""):
                splitLine = line.split()
                command = splitLine[0]

                if(command == ("name:")):
                    name = splitLine[1]
                if (command == ("desc:")):
                    desc = line.lstrip("desc: ")
                if (command == ("projectID:")):
                    projectID = splitLine[1]
                if (command == ("users:")):
                    projectsArray = splitLine[1].split(',')
                    parsed = databaseModule.Project(name, desc, projectID, users)
                    projectList.append(parsed)
                    # add to the array of projects
        file.close()
        return projectList

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
