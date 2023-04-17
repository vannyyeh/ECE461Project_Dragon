from flask import Flask, request
from flask_cors import CORS
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


@app.route('/add_user/', methods=['POST'])
def add_user():
    username = request.json.get("username")
    password = request.json.get("password")
    userID = request.json.get("userID")
    response = ProjectDragon.add_user(username, password, userID)
    return response

@app.route('/get_user_projects/<userID>', methods=['GET'])
def get_user_projects(userID):
    response = ProjectDragon.get_user_projects(userID)
    return response

@app.route('/delete_user/<string:userID>', methods=['DELETE'])
def delete_user(userID):
    response = ProjectDragon.delete_user(userID)
    return response

@app.route('/add_project/', methods=['POST'])
def add_project():
    name = request.json.get("name")
    desc = request.json.get("desc")
    projectID = request.json.get("projectID")
    response = ProjectDragon.add_project(name, desc, projectID)
    return response

@app.route('/delete_project/<string:projectID>', methods=['DELETE'])
def delete_project(projectID):
    response = ProjectDragon.delete_project(projectID)
    return response

@app.route('/add_hardware_set/', methods=['POST'])
def add_hardware_set():
    hwID = request.json.get("hwID")
    name = request.json.get("name")
    capacity = request.json.get("capacity")
    availability = request.json.get("availability")
    response = ProjectDragon.add_hardware_set(hwID, name, capacity, availability)
    return response

@app.route('/patch_hardware_set/', methods=['PATCH'])
def patch_hardware_set():
    hwID = request.json.get("hwID")
    projectID = request.json.get("projectID")
    availabilityChange = request.json.get("availabilityChange")
    name = request.json.get("name")
    response = ProjectDragon.patch_hardware_set(hwID, projectID, availabilityChange, name)
    return response

@app.route('/delete_hardware_set/<string:hardwareID>', methods=['DELETE'])
def delete_hardware_set(hardwareID):
    response = ProjectDragon.delete_hardware_set(hardwareID)
    return response

@app.route('/user_join_project/', methods=['PATCH'])
def user_join_project():
    projectID = request.json.get("projectID")
    userID = request.json.get("userID")
    response = ProjectDragon.user_join_project(projectID, userID)
    return response

@app.route('/user_leave_project/', methods=['PATCH'])
def user_leave_project():
    projectID = request.json.get("projectID")
    userID = request.json.get("userID")
    response = ProjectDragon.user_leave_project(projectID, userID)
    return response

@app.route('/authorize_user/', methods=['PATCH'])
def authorize_user():
    projectID = request.json.get("projectID")
    userID = request.json.get("userID")
    response = ProjectDragon.authorize_user(projectID, userID)
    return response

@app.route('/unauthorize_user/', methods=['PATCH'])
def unauthorize_user():
    projectID = request.json.get("projectID")
    userID = request.json.get("userID")
    response = ProjectDragon.unauthorize_user(projectID, userID)
    return response

@app.route('/login_user/', methods=['PATCH'])
def login_user():
    userID = request.json.get("userID")
    password = request.json.get("password")
    response = ProjectDragon.login_user(userID, password)
    return response