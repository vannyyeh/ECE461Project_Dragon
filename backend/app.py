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

    