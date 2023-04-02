from flask import Flask, jsonify
import pymongo
import os
import json
import database

app = Flask(__name__)

ProjectDragon = database.Database("mongodb+srv://ProjectDragonUser:Z62xa7Vhmw3kHSkd@cluster0.bpaif8q.mongodb.net/?retryWrites=true&w=majority")

if __name__ == "__main__":
    app.run()



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


@app.route("/create_new_project/<string:projectID>/<string:projectName>/<string:userID>", methods=['POST'])
def create_new_project(projectID, desc, projectName, userID):

    print("creating new project")

    response = None
    new_project= {
        'projectID': projectID,
        'desc': desc,
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


@app.route("/check_login_attempt/<string:username>/<string:userID>", methods=["GET"])
def check_login_attempt(username, password, userID):
    response = jsonify(
        msg=userID + " not exist",
        status=204
    )

@app.route("/create_user/<string:username>/<string:userID>", methods=["POST"])
def create_user(username, password, userID, projects):
    print("creating new user")
    response = ProjectDragon.add_user(username, password, userID, projects)
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost')
    return response

    