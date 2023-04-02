from flask import Flask, jsonify
import pymongo
import os
import json

app = Flask(__name__)

try:
    # setup mongodb
    mongodbClient = pymongo.MongoClient(
        "mongodb+srv://ProjectDragonUser:Z62xa7Vhmw3kHSkd@cluster0.bpaif8q.mongodb.net/?retryWrites=true&w=majority", serverSelectionTimeoytMS = 1000)
    db = mongodbClient.ProjectDragon
    hwsets = db["HardwareSets"]
    users = db["Users"]
    projects = db["Projects"]

    mongodbClient.server_info() # to Trigger except if needed

except:
    print("Error Connecting to Database")

if __name__ == "__main__":
    app.run()



@app.route('/joinProject/<int:projectID>/<string:userID>', methods=['PATCH'])
def joinProject(projectId, userId):
    project = projects.find({"projectID": projectId})

    response = None
    if project:
        users = project.get('userID', [])
        if userId not in users:
            users.append(userId)
            project.update_one({"projectID": projectId}, {"$set": {"userID": users}})

        response = jsonify(
            msg="Joined {projectId}",
            status=200
        )

    else:
        response = jsonify(
            msg="{projectId} not exist",
            status=204
        )

    response.headers.add('Access-Control-Allow-Origin', 'http://localhost')    
    return response


@app.route('/leaveProject/<int:projectID>/<string:userID>', methods=['PATCH'])
def leaveProject(projectId, userId):
    all_projects = projects.find({"projectID": projectId})

    if all_projects:
        users = all_projects.get('userID', [])
        if userId in users:
            users.remove(userId)
            all_projects.update_one({"projectID": projectId}, {"$set": {"userID": users}})
            return f'{userId} left {projectId}'
        else:
            return f'{userId} is not a user in project {projectId}'
    else:
        return f'{projectId} does not exist'


@app.route("/createNewProject/<string:projectID>/<string:projectName>/<string:userID>", methods=['POST'])
def createNewProject(projectID, projectName, userID):

    print("creating new project")

    response = None
    new_project= {
        'projectID': projectID,
        'projectName': projectName,
        'users': userID
    }

    if projects.find({"ProjectID": projectID}) == None:
        projects.insert_one(new_project)
        response = jsonify(
            msg="New {projectName} lunched!",
            status=200
        )

    else:
        response = jsonify(
            msg="project already exits",
            status=204
        )
    
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost')    
    return response


@app.route("/validateLogin/<string:username>/<string:userID>", methods=["GET"])
def checkLoginAttempt(username, password, userID):
    try:
        targetUser = users.find({"username": username, "password": password, "userID": userID})
        return json.dumps(True)
    except Exception as ex:
        print(ex)
        return json.dumps(False)


@app.route("/createUser/<string:username>/<string:userID>", methods=["POST"])
def createUser(username, password, userID):

    print("creating new project")

    response = None
    new_user= {
        'userID': userID,
        'username': username,
        'password': password
    }

    if users.find({"userID": userID}) == None:
        users.insert_one(new_user)
        response = jsonify(
            msg="New user added!",
            status=201
        )

    else:
        response = jsonify(
            msg="user with userID {userID} already exits",
            status=204
        )
    
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost')    
    return response


@app.route('/checkin/<string:projectID>/<string:hwsetsname>/<int:qty>')
def checkIn_hardware(projectId, hwsetname, qty):
    hwset_query = {"Name": hwsetname}
    hwset_document = hwsets.find(hwset_query)
    available_units = hwset_document["Availability"]
    capacity_units = hwset_document["Capacity"]
    project = projects.find_one({"ProjectID": projectId})
    project_hardware = project['HWSets']

    project = projects.find({"ProjectID": projectId})
    if qty > capacity_units:
        qty_checked_in = capacity_units - available_units
    else:
        qty_checked_in = qty


    projects.update_one({"ProjectID": projectId}, {"$set": {"HWSet": project_hardware}})
    hwsets.update_one({"Name": hwsetname}, {"$set": {"Availability": qty_checked_in + available_units}})

    return {
        'projectId': projectId,
        'hwsetsname': hwsetname,
        'qty': qty,
    }

@app.route('/checkout/<string:projectID>/<string:hwsetsname>/<int:qty>')
def checkOut_hardware(projectId, hwsetname, qty):
    return 'come back and edit'
