from flask import Flask, jsonify
import json
import pymongo
import databaseModule
import encrypt


class Database:

    # Initialization Begins
    def __init__(self, serverURL):

        self.__mongodbClient = None
        self.__db = None
        self.__hwCollections = None
        self.__usersCollections = None
        self.__projectsCollections = None

        try:
            # setup mongodb
            self.__mongodbClient = pymongo.MongoClient(serverURL)
            self.__db = self.__mongodbClient.ProjectDragon
            self.__hwCollections = self.__db["HardwareSets"]
            self.__usersCollections = self.__db["Users"]
            self.__projectsCollections = self.__db["Projects"]

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

    def add_user(self, username, password, userID, projects = []):

        response = None
        password = encrypt.encrypt(password)
        
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
            )
            response.status=204
            return response
        else:
            # no user with that ID
            self.__usersCollections.insert_one(new_user)
            response = jsonify(
                msg="User " + userID + " added",
            )
            response.status=201
            return response

    def user_existence(self, userID):
        user = self.__usersCollections.find_one({"userID": userID})
        if user:
            return True
        else:
            return False

    def login_user(self, userID, password):
        user = self.__usersCollections.find_one({"userID": userID})
        realPassword = encrypt.decrypt(user["password"])
        if realPassword == password:
            response = jsonify(
                msg="User " + userID + " logged in",
            )
            response.status=200
            return response
        else:
            response = jsonify(
                msg="User " + userID + " login unsuccessful",
            )
            response.status=204
            return response

    def delete_user(self, userID):
        response = None

        userExistance = self.user_existence(userID)
        
        if userExistance:
            # user exists with that ID

            self.__usersCollections.delete_one({"userID": userID})

            response = jsonify(
                msg="User " + userID + " deleted",
            )
            response.status=200
            return response
        else:
            # no user with that ID

            response = jsonify(
                msg="User " + userID + " does not exist",
            )
            response.status=204
            return response

    # User Dictionary Manipulation End
    # HardwareSet Dictionary Manipulation Begin

    def add_hardware_set(self, hwID, name, capacity, availability):

        response = None
        
        new_hardware_set = {    
            'hwID': hwID,
            'name': name,
            'capacity': capacity,
            'availability': availability,
            'tiedProjects': []
        }

        hardwareSetExistence = self.hardware_set_existence(hwID)
        
        if hardwareSetExistence:
            # hardware_set already exists with that ID
            print("hardware set exists")
            response = jsonify(
                msg="Hardware Set " + hwID + " already exists",
            )
            response.status=200
            return response
        else:
            # no hardware_set with that ID
            print("creating hardware set")
            self.__hwCollections.insert_one(new_hardware_set)
            response = jsonify(
                msg="Hardware Set " + hwID + " added",
            )
            response.status=201
            return response
        
    def patch_hardware_set(self, hwID, projectID, strAvailabilityChange, name = None):

        response = None

        hardwareSetExistence = self.hardware_set_existence(hwID)
        
        if hardwareSetExistence:
            # hardware_set already exists with that ID
            hardware_set = self.__hwCollections.find_one({"hwID": hwID})
            capacity = hardware_set['capacity']
            availability = hardware_set['availability']
            availabilityChange = int(strAvailabilityChange)
            if ((availability + availabilityChange > capacity) or (availability + availabilityChange < 0)):
                response = jsonify(
                    msg="Bad request, availability greater than capacity",
                )
                response.status=400
                return response
            
            tied_projects = hardware_set['tiedProjects']

            in_tied_projects = False
            for i in range(len(tied_projects)):
                if (tied_projects[i][0] == projectID):
                    in_tied_projects = True

            if in_tied_projects:
                tied_projects[i][1] = tied_projects[i][1] + availabilityChange
                self.__hwCollections.update_one({"hwID": hwID}, {"$set": {"tiedProjects": tied_projects}})
            else:
                new_tied_projects = []
                for i in range(len(tied_projects)):
                    new_tied_projects.append(tied_projects[i])
                new_tied_projects.append([projectID, availabilityChange])
                self.__hwCollections.update_one({"hwID": hwID}, {"$set": {"tiedProjects": new_tied_projects}})


            if (self.project_existence(projectID)):
                grabbed_project = self.__projectsCollections.find_one({"projectID": projectID})
                grabbed_hardware_sets = grabbed_project['grabHW']

                in_grabbed_hardware_sets = False
                for i in range(len(grabbed_hardware_sets)):
                    if (grabbed_hardware_sets[i][0] == hwID):
                        in_grabbed_hardware_sets = True

                if in_grabbed_hardware_sets:    
                    grabbed_hardware_sets[i][1] = grabbed_hardware_sets[i][1] + availabilityChange
                    self.__projectsCollections.update_one({"projectID": projectID}, {"$set": {"grabHW": grabbed_hardware_sets}})
                else:
                    new_grabbed_hardware_sets = []
                    for i in range(len(grabbed_hardware_sets)):
                        new_grabbed_hardware_sets.append(grabbed_hardware_sets[i])
                    new_grabbed_hardware_sets.append([hwID, availabilityChange])
                    self.__projectsCollections.update_one({"projectID": projectID}, {"$set": {"grabHW": new_grabbed_hardware_sets}})
                    
            else:
                if (projectID is not None):
                    response = jsonify(
                        msg="Project does not exist",
                    )
                    response.status=400
                    return response

            self.__hwCollections.update_one({"hwID": hwID}, {"$set": {"availability": availability + availabilityChange}})

            if name is not None:
                self.__hwCollections.update_one({"hwID": hwID}, {"$set": {"name": name}})
                

            hardware_set = self.__hwCollections.find_one({"hwID": hwID})
            print(hardware_set)
            response = jsonify(
                msg="Hardware Set " + hwID + " updated!",
            )
            response.status=200
            return response
        else:
            # no hardware_set with that ID
            response = jsonify(
                msg="Hardware Set " + hwID + " does not exist!",
            )
            response.status=201
            return response

    def hardware_set_existence(self, hwID):
        hardware_set = self.__hwCollections.find_one({"hwID": hwID})
        if hardware_set:
            return True
        else:
            return False

    def delete_hardware_set(self, hwID):
        response = None

        hardwareSetExistance = self.hardware_set_existence(hwID)

        if hardwareSetExistance:
            # user exists with that ID

            hardware_set = self.__hwCollections.find_one({"hwID": hwID})
            tied_projects = hardware_set.get("tiedProjects")
            for tied_project in tied_projects:
                self.patch_hardware_set(hwID, tied_project[0], -1 * int(tied_project[1]))

            self.__hwCollections.delete_one({"hwID": hwID})

            response = jsonify(
                msg="Hardware Set " + hwID + " deleted",
            )
            response.status=200
            return response
        else:
            # no user with that ID

            response = jsonify(
                msg="Hardware Set " + hwID + " does not exist",
            )
            response.status=204
            return response

    # HardwareSet Dictionary Manipulation End
    # Project Dictionary Manipulation Begin

    def add_project(self, name, desc, projectID, users = [], grabHW = []):

        response = None
        
        new_project = {  
            'name': name,
            'desc': desc,
            'projectID': projectID,
            'users': users,
            'grabHW': grabHW
        }

        projectExistance = self.project_existence(projectID)
        
        if projectExistance:
            # user already exists with that ID
            response = jsonify(
                msg="Project " + projectID + " already exists",
            )
            response.status=204
            return response
        else:
            # no user with that ID
            self.__projectsCollections.insert_one(new_project)
            response = jsonify(
                msg="Project " + projectID + " added",
            )
            response.status=201
            return response

    def project_existence(self, projectID):
        project = self.__projectsCollections.find_one({"projectID": projectID})
        if project:
            return True
        else:
            return False

    def delete_project(self, projectID):
        response = None

        projectExistance = self.project_existence(projectID)

        if projectExistance:
            # user exists with that ID

            project = self.__projectsCollections.find_one({"projectID": projectID})
            grabbed_hardware_sets = project.get("grabHW")
            for grabbed_set in grabbed_hardware_sets:
                self.patch_hardware_set(grabbed_set[0], projectID, -1 * int(grabbed_set[1]))

            self.__projectsCollections.delete_one({"projectID": projectID})

            response = jsonify(
                msg="Project " + projectID + " deleted",
            )
            response.status=200
            return response
        else:
            # no user with that ID

            response = jsonify(
                msg="Project " + projectID + " does not exist",
            )
            response.status=204
            return response

    def user_join_project(self, projectID, userID):
        response = None

        userExistance = self.user_existence(userID)
        projectExistance = self.project_existence(projectID)

        if projectExistance and userExistance:
            user = self.__usersCollections.find_one({"userID": userID})
            print(user)
            acceptableUsers = self.__projectsCollections.find_one({"projectID": projectID}).get("users")
            
            in_acceptable_users = False
            for acceptableUser in acceptableUsers:
                if userID == acceptableUser:
                    # authorized user
                    in_acceptable_users = True

            if in_acceptable_users:
                joinedProjects = user.get('projects', [])
                print("joined projects")
                print(joinedProjects)
                # add project to user projects

                if projectID in joinedProjects:
                    response = jsonify(
                        msg="" + projectID + " already in " + userID + " joined projects",
                        status=204
                    )
                    return response

                joinedProjects.append(projectID)
                self.__usersCollections.update_one({"userID": userID}, {"$set": {"projects": joinedProjects}})

                response = jsonify(
                    msg=userID + " Joined " + projectID,
                    status=200
                )
                return response

            else:
                # user is not authorized
                response = jsonify(
                    msg=userID + " Not Authorized to Join " + projectID,
                    status=401
                )
                return response

        else:
            response = jsonify(
                msg="" + str(projectID) + " or " + userID + " does not exist",
                status=204
            )
            return response

    def user_leave_project(self, projectID, userID):
        response = None

        userExistance = self.user_existence(userID)
        projectExistance = self.project_existence(projectID)

        if projectExistance and userExistance:

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
            self.__usersCollections.update_one({"userID": userID}, {"$set": {"projects": joinedProjects}})

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

    def unauthorize_user(self, projectID, userID):
        response = None

        userExistance = self.user_existence(userID)
        projectExistance = self.project_existence(projectID)

        if projectExistance and userExistance:

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
            self.__projectsCollections.update_one({"projectID": projectID}, {"$set": {"users": authorizedUsers}})

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
        if (projectExistance) and (userExistance):

            targetProject = self.__projectsCollections.find_one({"projectID": projectID})
            print(targetProject)
            authorizedUsers = targetProject.get('users', [])
            # remove project from user projects

            if userID in authorizedUsers:
                response = jsonify(
                    msg=userID + " already in " + projectID + " authorized users",
                    status=204
                )
                return response

            authorizedUsers.append(userID)
            self.__projectsCollections.update_one({"projectID": projectID}, {"$set": {"users": authorizedUsers}})

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
