from flask import Flask, jsonify
import json
import pymongo
import databaseModule


class Database:

    # Initialization Begins
    def __init__(self, serverURL):

        self. __mongodbClient = None
        self.__db = None
        self.__hwCollections = None
        self.__usersCollections = None
        self.__projectsCollections = None

        try:
            # setup mongodb
            self.__mongodbClient = pymongo.MongoClient(
                serverURL,
                serverSelectionTimeoutMS=1000)
            self.__db = self.__mongodbClient.ProjectDragon
            self.__hwCollections = self.__db["HardwareSets"]
            self.__usersCollections = self.__db["Users"]
            self.__projectsCollections = self.__db["Projects"]

            self.__mongodbClient.server_info()  # to Trigger except if needed

        except:
            print("Error Connecting to Database")

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

    def parse_hwSets(self, filename):
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

    def add_user(self, username, password, userID, projects):

        response = None

        new_user = {
            'userID': userID,
            'username': username,
            'password': password,
            'projects': projects
        }

        userExistance = self.user_existence(userID)

        if userExistance:
            # user already exists with that ID

            response = jsonify(
                msg="User " + userID + " already exists",
                status=204
            )
            return response
        else:
            # no user with that ID

            self.__usersCollections.insert_one(new_user)

            response = jsonify(
                msg="User " + userID + " added",
                status=201
            )
            return response

    def user_existence(self, userID):

        user = self.__usersCollections.find_one({"userID": userID})

        if user:
            return True
        else:
            return False

    def delete_user(self, userID):
        response = None

        userExistance = self.user_existence(userID)

        if userExistance:
            # user exists with that ID

            user = self.__usersCollections.delete({"userID": userID})

            response = jsonify(
                msg="User " + userID + " deleted",
                status=200
            )
            return response
        else:
            # no user with that ID

            response = jsonify(
                msg="User " + userID + " does not exist",
                status=204
            )
            return response

    def get_user(self, userID):
        response = None
        userExistance = self.user_existence(userID)

        if userExistance:
            # user exists
            response = self.__usersCollections.find_one({"userID": userID})
            print(response)

            return response
        else:
            # no user exists
            return response

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

    def add_project(self, name, desc, projectID, users):


        response = None

        new_project = {
            'name': name,
            'desc': desc,
            'projectID': projectID,
            'users': users
        }

        projectExistance = self.project_existence(projectID)

        if projectExistance:
            # user already exists with that ID

            response = jsonify(
                msg="Project " + projectID + " already exists",
                status=204
            )
            return response
        else:
            # no user with that ID

            self.__usersCollections.insert_one(new_project)

            response = jsonify(
                msg="Project " + projectID + " added",
                status=201
            )
            return response

    def project_existence(self, projectID):

        project = self.__projectsCollections.find_one({"projectID": projectID})

        if project:
            return True
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

    def user_join_project(self, projectID, userID):
        response = None

        userExistance = self.user_existence(userID)
        projectExistance = self.project_existence(projectID)

        if not userExistance:
            # user does not exist
            response = jsonify(
                msg=userID + " does not exist",
                status=204
            )

        if projectExistance:
            user = self.__usersCollections.find_one({"userID": userID})
            print(user)
            acceptableUsers = self.__projectsCollections.find_one({"projectID": projectID}).get("userIDs")

            if userID in acceptableUsers:
                # authorized user

                joinedProjects = user.get('projects', [])
                # add project to user projects

                if projectID in joinedProjects:
                    response = jsonify(
                        msg=projectID + " already in " + userID + " joined projects",
                        status=204
                    )
                    return response

                joinedProjects.append(projectID)
                user.update_one({"userID": userID}, {"$set": {"projects": joinedProjects}})

                response = jsonify(
                    msg=userID + " Joined " + projectID,
                    status=200
                )
                return response

            else:
                # user is not authorized
                response = jsonify(
                    msg=userID + + " Not Authorized to Join " + projectID,
                    status=401
                )
                return response

        else:
            response = jsonify(
                msg=projectID + " does not exist",
                status=204
            )
            return response

    def user_leave_project(self, projectID, userID):
        response = None

        userExistance = self.user_existence(userID)
        projectExistance = self.project_existence(projectID)

        if not userExistance:
            # user does not exist
            response = jsonify(
                msg=userID + " does not exist",
                status=204
            )

            return response

        if projectExistance:

            user = self.__usersCollections.find_one({"userID": userID})
            print(user)
            joinedProjects = user.get('projects', [])
            # remove project from user projects

            if projectID not in joinedProjects:
                response = jsonify(
                    msg=projectID + " not in " + userID + " joined projects",
                    status=204
                )
                return response

            joinedProjects.remove(projectID)
            user.update_one({"userID": userID}, {"$set": {"projects": joinedProjects}})

            response = jsonify(
                msg=userID + " Left " + projectID,
                status=200
            )

            return response

        else:
            response = jsonify(
                msg=projectID + " does not exist",
                status=204
            )

            return response

    def unauthrize_user(self, projectID, userID):
        response = None

        userExistance = self.user_existence(userID)
        projectExistance = self.project_existence(projectID)

        if not userExistance:
            # user does not exist
            response = jsonify(
                msg=userID + " does not exist",
                status=204
            )

            return response

        if projectExistance:

            targetProject = self.__projectsCollections.find_one({"projectID": projectID})
            print(targetProject)
            authorizedUsers = targetProject.get('users', [])
            # remove project from user projects

            if userID not in authorizedUsers:
                response = jsonify(
                    msg=userID + " not in " + projectID + " authoized users",
                    status=204
                )
                return response

            authorizedUsers.remove(userID)
            targetProject.update_one({"projectID": projectID}, {"$set": {"users": authorizedUsers}})

            response = jsonify(
                msg=userID + " Unauthorized For " + projectID,
                status=200
            )

            return response

        else:
            response = jsonify(
                msg=projectID + " does not exist",
                status=204
            )

            return response

    def authorize_user(self, projectID, userID):
        response = None

        userExistance = self.user_existence(userID)
        projectExistance = self.project_existence(projectID)

        if not userExistance:
            # user does not exist
            response = jsonify(
                msg=userID + " does not exist",
                status=204
            )

            return response

        if projectExistance:

            targetProject = self.__projectsCollections.find_one({"projectID": projectID})
            print(targetProject)
            authorizedUsers = targetProject.get('users', [])
            # remove project from user projects

            if userID in authorizedUsers:
                response = jsonify(
                    msg=userID + " already in " + projectID + " authoized users",
                    status=204
                )
                return response

            authorizedUsers.append(userID)
            targetProject.update_one({"projectID": projectID}, {"$set": {"users": authorizedUsers}})

            response = jsonify(
                msg=userID + " Authorized For " + projectID,
                status=200
            )

            return response

        else:
            response = jsonify(
                msg=projectID + " does not exist",
                status=204
            )

            return response
