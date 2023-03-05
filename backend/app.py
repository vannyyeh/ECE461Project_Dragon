from flask import Flask

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/")
def test():
    return "NO SHOT, WOAH A FLASK APP??!?!"

@app.route("/get_this", methods=['GET'])
def testGet():
    getData = {"msg": "no shot, a json message?"}
    return getData

#todo: Alright Milton, this 