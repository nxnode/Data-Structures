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
