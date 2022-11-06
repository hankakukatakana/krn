from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/gas")
def hello_world():
    return render_template('gas.html')

@app.route("/denki")
def hello_world():
    return render_template('denki.html')

@app.route("/suidou")
def hello_world():
    return render_template('suidou.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost', port=5000)

