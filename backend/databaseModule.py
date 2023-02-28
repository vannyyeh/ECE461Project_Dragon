class User:

    def __init__(self, username, userID, password, projectsArray):
        self.__username = username
        self.__userID = userID
        self.__password = password
        self.__projectsArray = projectsArray


class HardwareSet:

    def __init__(self, capacity, availability, requested):
        self.__capacity = capacity
        self.__availability = availability
        self.__requested = requested


class Project:
    def __init__(self, name, description, projectID):
        self.__name = name
        self.__description = description
        self.__projectID = projectID
