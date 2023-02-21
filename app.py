from flask import Flask, request

app = Flask(__name__)


@app.route("/abc/")
def hello_world():
    return {"hello": "world"}


@app.route("/def/")
def hello_other():
    print(request.query_string)
    print(request.args)
    print(request.args["abc"])
    return "other"


@app.route("/echo/", methods=["POST"])
def echo():
    print(dir(request))
    print(request.data)
    data = request.json
    data = {value: key for key, value in data.items()}
    return data
