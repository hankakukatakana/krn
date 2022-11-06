from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def lifeline():
    return render_template('lifeline.html' )

@app.route("/gas")
def gas():
    return render_template('gas.html' )

@app.route("/denki")
def denki():
    return render_template('denki.html')

@app.route("/suidou")
def suidou():
    return render_template('suidou.html')

@app.route("/test")
def test():
    return render_template('test.html')


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=6000)