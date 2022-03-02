from flask import Flask, jsonify, request

from he import h,h2

app = Flask(__name__)

def sum():
    a=10
    b=10
    c=a+b
    return c

@app.route("/", methods=['GET', 'POST'])
def hello_world():

    if request.method == 'POST':
        return jsonify(metode = "POST")
    else:
        return jsonify(method = "GET")


@app.route("/atanu")
@app.route("/atanu/<name>")
def hello(name=None):
    h();
    h2();
    return { "username" : "pl"}

if __name__=="__main__":
    app.run(port=8080)