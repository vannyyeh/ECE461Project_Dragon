from flask import Flask
import pymongo

app = Flask(__name__)

try:
    # setup mongodb
    mongodbClient = pymongo.MongoClient(
        "mongodb+srv://ProjectDragonUser:Z62xa7Vhmw3kHSkd@cluster0.bpaif8q.mongodb.net/?retryWrites=true&w=majority", serverSelectionTimeoytMS = 1000)
    db = mongodbClient.ProjectDragon
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
