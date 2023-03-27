from flask import Flask, jsonify, request, render_template
import pymongo
import os
import json
from bson import json_util
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



@app.route("/") #root
def test():
    return "NO SHOT, WOAH A FLASK APP??!?!"

@app.route("/get_this", methods=['GET'])
def testGet():
    getData = {"msg": "no shot, a json message?"}
    return getData

@flask_app.route('/join/<int:projectID>/<string:userID>')
def joinProject(projectId, userId):
    all_projects = projects.find({"projectID": projectId})

    if all_projects:
        users = all_projects.get('userID', [])
        if userId not in users:
            users.append(userId)
            all_projects.update_one({"projectID": projectId}, {"$set": {"userID": users}})
        return f'Joined {projectId}'
    else:
        return f'{projectId} not exist'


@flask_app.route('/leave/<int:projectID>/<string:userID>')
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


@app.route("/createnewproject/<string:projectID>/<string:projectName>/<string:userID>")
def createNewProject(projectID, projectName, userID):
    new_project= {
        'ProjectID': projectID,
        'ProjectName': projectName,
        'Users': userID,
        'HWSets': {'HWSet1': 0, 'HWSet2': 0},
    }

    if projects.find({"ProjectID": projectID}) != None:
        return{
            'error' :'project already exits'
        }

    else:
        projects.insert_one(new_project)
        return{
            f'New {projectName} lunched!'
        }
