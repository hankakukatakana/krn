from flask import Flask
from flask import render_template
from krn import db

app = Flask(__name__)

@app.route("/")
def lifeline():
    return render_template('lifeline.html')

@app.route("/gas")
def gas():
    name = 'Gas'
    return render_template('category.html', name=name)

@app.route("/denki")
def denki():
    name = 'Denki'
    return render_template('category.html', name=name)

@app.route("/suidou")
def suidou():
    name = 'Suidou'
    return render_template('category.html', name=name)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=6000)