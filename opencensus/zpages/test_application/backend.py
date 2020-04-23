from flask import Flask, escape, request, render_template, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/getdata1')
def getData1():
    name = "Anam Navied"
    test_data = {'name': name}
    return test_data

@app.route('/getdata2')
def getData2():
    name = "Gaven Kerr"
    test_data = {'name': name}
    return test_data

@app.route('/getdata3')
def getData3():
    name = "Aasiyah Feisal"
    test_data = {'name': name}
    return test_data



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)