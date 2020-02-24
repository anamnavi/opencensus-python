from flask import Flask, escape, request, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    names = {'name1': "Anam", 'name2': "Gaven", "name3": "Aasiyah"}
    return render_template("index.html", names=names)

@app.route('/getmethod1', methods=['GET'])
def getData1():
    name = "Anam Navied"
    test_data = {'name': name}
    return test_data

@app.route('/getmethod2', methods=['GET'])
def getData2():
    name = "Gaven Kerr"
    test_data = {'name': name}
    return test_data

@app.route('/getmethod3', methods=['GET'])
def getData3():
    name = "Aasiyah Feisal"
    test_data = {'name': name}
    return test_data


if __name__ == '__main__':
    app.run(debug=True)