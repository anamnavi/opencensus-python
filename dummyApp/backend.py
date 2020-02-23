from flask import Flask, escape, request, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    names = {'name1': "Anam", 'name2': "Gaven", "name3": "Aasiyah"}
    return render_template("index.html", names=names)


if __name__ == '__main__':
    app.run(debug=True)