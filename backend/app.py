from flask import Flask, jsonify
from flask_cors import CORS
import pymongo
import os
import json
import database


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

mongodbClient = None
db = None
hwsets = None
users = None
projects = None

ProjectDragon = database.Database("mongodb+srv://ProjectDragonUser:Z62xa7Vhmw3kHSkd@cluster0.bpaif8q.mongodb.net/?retryWrites=true&w=majority")

if __name__ == "__main__":
    app.run()

@app.route('/test_backend/<int:projectID>/<string:userID>', methods=['POST'])
def testBackend(projectID, userID):
    
    response = jsonify(
        msg="" + str(projectID) + ": " + str(userID) + str(mongodbClient),
        status=200
    )

    return response


@app.route('/join_project/<int:projectID>/<string:userID>', methods=['PATCH'])
def join_project(projectId, userId):
    response = ProjectDragon.user_join_project(projectId, userId)
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost')
    return response


@app.route('/leave_project/<int:projectID>/<string:userID>', methods=['PATCH'])
def leave_project(projectId, userId):
    response = ProjectDragon.user_leave_project(projectId, userId)
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost')
    return response


@app.route("/create_new_project/<string:projectName>/<string:projectID>/", methods=['POST'])
def create_new_project(projectName, desc, projectID, users):
    print("creating new project")
    response = ProjectDragon.add_project(projectName, desc, projectID, users)
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost')    
    return response


@app.route("/check_login_attempt/<string:username>/<string:userID>", methods=["GET"])
def check_login_attempt(username, password, userID):
    response = None
    targetUser = ProjectDragon.get_user(userID)

    if targetUser is not None:

        correctUsername = username == targetUser.get(str(username))
        correctPassword = password == targetUser.get(str(password))
        correctLogin = correctUsername and correctPassword

        if correctLogin:
            response = jsonify(
                msg="Login Success",
                result=True,
                status=200
            )
            return response
        else:
            response = jsonify(
                msg="Incorrect Login",
                result=False,
                status=400
            )
            return response

    else:
        response = jsonify(
            msg=userID + " does not exist",
            result=False,
            status=204
        )
        return response

@app.route("/create_user/<string:username>/<string:userID>", methods=["POST"])
def create_user(username, password, userID, projects):
    print("creating new user")
    response = ProjectDragon.add_user(username, password, userID, projects)
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
