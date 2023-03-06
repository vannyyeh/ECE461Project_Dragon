class User:

    def __init__(self, username, userID, password, projectsArray):
        self.__username = username
        self.__userID = userID
        self.__password = password
        self.__projectsArray = projectsArray

    def get_userID(self):
        return self.__userID


class HardwareSet:

    def __init__(self, name, capacity, availability, requested):
        self.__name = name
        self.__capacity = capacity
        self.__availability = availability
        self.__requested = requested

    def get_hw_name(self):
        return self.__name


class Project:
    def __init__(self, name, description, projectID, acceptedUsers):
        self.__name = name
        self.__description = description
        self.__projectID = projectID
        self.__acceptedUsers = acceptedUsers

    def get_projectID(self):
        return self.__projectID

    def valid_user_check(self, userID):
        if userID in self.__acceptedUsers:
            return True
        else:
            return False
