from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def lifeline():
    return render_template('lifline.html' )

@app.route("/gas")
def gas():
    return render_template('gas.html' )

@app.route("/denki")
def denki():
    return render_template('denki.html')

@app.route("/suidou")
def suidou():
    return render_template('suidou.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost', port=5000)